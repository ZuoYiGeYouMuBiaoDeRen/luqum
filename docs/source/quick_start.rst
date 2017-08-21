Quick start
===========

    >>> from unittest import TestCase
    >>> t = TestCase()


.. _tutorial-parsing:

Parsing
-------

To parse a query you need to import the parser, and give it a string to parse::

    >>> from luqum.parser import parser
    >>> tree = parser.parse('(title:"foo bar" AND body:"quick fox") OR title:fox')

You'll get an object which is a tree, made of the elements composing the query::

    >>> print(repr(tree))
    OrOperation(Group(AndOperation(SearchField('title', Phrase('"foo bar"')), SearchField('body', Phrase('"quick fox"')))), SearchField('title', Word('fox')))

This can be viewed like that:

.. graphviz::

   digraph foo {
     or1 [label="OrOperation"];
     group1 [label="Group"];
     and1 [label="AndOperation"];
     search_title1 [label="SearchField\ntitle"];
     foo_bar [label="Phrase\nfoo bar"];
     search_body [label="SearchField\nbody"];
     quick_fox [label="Phrase\nquick fox"];
     search_title2 [label="SearchField\ntitle"];
     fox [label="Word\nfox"];
     or1 -> group1;
     or1 -> search_title2;
     group1 -> and1;
     and1 -> search_title1;
     and1 -> search_body;
     search_title1 -> foo_bar;
     search_body -> quick_fox;
     search_title2 -> fox;
   }


You can convert it back to a query using the standard ``str`` method from python::

    >>> print(str(tree))
    (title:"foo bar" AND body:"quick fox") OR title:fox

Manipulating
------------

One of the goal of luqum is to be able to manipulate queries.

In the previous request we can modify ``"foo bar"`` for ``"lazy dog"``::

    >>> tree.children[0].children[0].children[0].children[0].value = '"lazy dog"'
    >>> print(str(tree))
    (title:"lazy dog" AND body:"quick fox") OR title:fox

That was a bit tedious. Of course, normally you will use recursion and visitor pattern
to do such things.

Luqum does provide some helpers for this::

    >>> from luqum.utils import LuceneTreeTransformer
    >>> class MyTransformer(LuceneTreeTransformer):
    ...     def visit_search_field(self, node, parents):
    ...         if node.expr.value == '"lazy dog"':
    ...             node.expr.value = '"back to foo bar"'
    ...         return node
    ...
    >>> transformer = MyTransformer()
    >>> new_tree = transformer.visit(tree)
    >>> print(str(new_tree))
    (title:"back to foo bar" AND body:"quick fox") OR title:fox

.. _tutorial-elastic:

Transforming to elastic query
-----------------------------

Luqum also offers you to transform Lucene queries to `Elasticsearch queries DSL`_.

This is useful to extend capacities of Lucene queries and get the best out of elastic search.

To help interpret the requests,
we need to pass a list of fields to consider as terms (as opposed to full text searches).
We may also pass default operator, and default fields::

   >>> from luqum.elasticsearch import ElasticsearchQueryBuilder
   >>> es_builder = ElasticsearchQueryBuilder(not_analyzed_fields=["published", "tag"])

   >>> tree = parser.parse('''
   ...     title:("brown fox" AND quick AND NOT dog) AND
   ...     published:[* TO 1990-01-01T00:00:00.000Z] AND
   ...     tag:fable
   ...     ''')
   >>> query = es_builder(tree)
   >>> t.assertDictEqual(
   ...     query,
   ...     {'bool': {'must': [
   ...         {'bool': {'must': [
   ...             {'match_phrase': {'title': {'query': 'brown fox'}}},
   ...             {'match': {'title': {'query': 'quick',
   ...                                  'type': 'phrase',
   ...                                  'zero_terms_query': 'all'}}},
   ...             {'bool': {'must_not': [{'match': {'title': {'query': 'dog',
   ...                                                         'type': 'phrase',
   ...                                                         'zero_terms_query': 'none'}}}]}}]}},
   ...         {'range': {'published': {'lte': '1990-01-01T00:00:00.000Z'}}},
   ...         {'term': {'tag': {'value': 'fable'}}}]}})

You may also use nested fields::

   >>> es_builder = ElasticsearchQueryBuilder(
   ...     nested_fields={"author": {"given_name", "last_name"}})
   >>> tree = parser.parse('''
   ...     title:"quick brown fox" AND
   ...     author:(given_name:Ja* AND last_name:London)
   ...     ''')
   >>> query = es_builder(tree)
   >>> t.assertDictEqual(
   ...     query,
   ...     {'bool': {'must': [
   ...         {'match_phrase': {'title': {'query': 'quick brown fox'}}},
   ...         {'nested': {
   ...             'query': {'bool': {'must': [
   ...                 {'query_string': {
   ...                     'default_field': 'author.given_name',
   ...                     'analyze_wildcard': True,
   ...                     'query': 'Ja*',
   ...                     'allow_leading_wildcard': True}},
   ...                 {'match': {'author.last_name': {
   ...                     'query': 'London',
   ...                     'type': 'phrase',
   ...                     'zero_terms_query': 'all'}}}]}},
   ...             'path': 'author'}}]}})

You can use this JSON directly with `elasticsearch python bindings`_,
but also use it to build query with `elasticsearch_dsl`_.

.. note::
   The list of terms fields could, of course,
   be automatically deduced from the elasticsearch schema

   Also there are some limitations to this transformation.
   Please, refers to the API :ref:`elasticsearch-api`
   

Note that under the hood, the operation is too fold:
it first create a new specific tree from the luqum tree.
This tree is then capable of giving it's JSON like represetation
(that is JSON compatible python objects).

.. _tutorial-unknown-operation:


The unknown operation
----------------------

In query you may use an implicit operator
leaving a blank between two expressions instead of OR or AND.
Because the meaning of this operator is unknown at parsing time,
it is replaced by a special ``UnknownOperator`` operation.

::

    >>> tree = parser.parse('foo bar')
    >>> tree
    UnknownOperation(Word('foo'), Word('bar'))

To help you deal with this we provide a transformer,
that will smartly replace ``UnkownOperation`` by ``AndOperation`` or ``OrOperation``.

    >>> from luqum.utils import UnknownOperationResolver
    >>> resolver = UnknownOperationResolver()
    >>> str(resolver(tree))
    'foo AND bar'

.. _tutorial-pretty-printing:

Pretty printing
---------------

Luqum also comes with a query pretty printer::

  >>> from luqum.pretty import prettify
  >>> tree = parser.parse(
  ...     'some_long_field:("some long value" OR "another quite long expression"~2 OR "even something more expanded"^4) AND yet_another_fieldname:[a_strange_value TO z]')
  >>> print(prettify(tree))
  some_long_field: (
      "some long value"
      OR
      "another quite long expression"~2
      OR
      "even something more expanded"^4
  )
  AND
  yet_another_fieldname: [a_strange_value TO z]


.. _`elasticsearch python bindings`: https://pypi.python.org/pypi/elasticsearch/
.. _`elasticsearch_dsl`: https://pypi.python.org/pypi/elasticsearch-dsl
.. _`Elasticsearch queries DSL`: https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html
