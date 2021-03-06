
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOR_OPleftAND_OPnonassocMINUSnonassocPLUSnonassocAPPROXnonassocBOOSTnonassocLPARENRPARENnonassocLBRACKETTORBRACKETnonassocPHRASEnonassocTERMAND_OP APPROX BOOST COLUMN LBRACKET LPAREN MINUS NOT OR_OP PHRASE PLUS RBRACKET RPAREN SEPARATOR TERM TOexpression : expression OR_OP expressionexpression : expression AND_OP expressionexpression : expression expressionunary_expression : PLUS unary_expressionunary_expression : MINUS unary_expressionunary_expression : NOT unary_expressionexpression : unary_expressionunary_expression : LPAREN expression RPARENunary_expression : LBRACKET phrase_or_term TO phrase_or_term RBRACKETunary_expression : TERM COLUMN unary_expressionunary_expression : PHRASEunary_expression : PHRASE APPROXexpression : expression BOOSTunary_expression : TERMunary_expression : TERM APPROXunary_expression : TOphrase_or_term : TERM\n                      | PHRASE'
    
_lr_action_items = {'PLUS':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,22,23,24,25,26,27,29,31,],[3,3,-7,3,3,3,3,-16,-14,-11,3,3,3,-13,-4,-5,-6,3,3,-15,-12,3,3,-8,-10,-9,]),'MINUS':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,22,23,24,25,26,27,29,31,],[4,4,-7,4,4,4,4,-16,-14,-11,4,4,4,-13,-4,-5,-6,4,4,-15,-12,4,4,-8,-10,-9,]),'NOT':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,22,23,24,25,26,27,29,31,],[5,5,-7,5,5,5,5,-16,-14,-11,5,5,5,-13,-4,-5,-6,5,5,-15,-12,-1,-2,-8,-10,-9,]),'LPAREN':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,22,23,24,25,26,27,29,31,],[6,6,-7,6,6,6,6,-16,-14,-11,6,6,6,-13,-4,-5,-6,6,6,-15,-12,6,6,-8,-10,-9,]),'LBRACKET':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,22,23,24,25,26,27,29,31,],[7,7,-7,7,7,7,7,-16,-14,-11,7,7,7,-13,-4,-5,-6,7,7,-15,-12,7,7,-8,-10,-9,]),'TERM':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,24,25,26,27,28,29,31,],[9,9,-7,9,9,9,9,20,-16,-14,-11,9,9,9,-13,-4,-5,-6,9,9,-15,-12,9,9,-8,20,-10,-9,]),'PHRASE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,22,23,24,25,26,27,28,29,31,],[10,10,-7,10,10,10,10,21,-16,-14,-11,10,10,10,-13,-4,-5,-6,10,10,-15,-12,10,10,-8,21,-10,-9,]),'TO':([0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,31,],[8,8,-7,8,8,8,8,-16,-14,-11,8,8,8,-13,-4,-5,-6,8,28,-17,-18,8,-15,-12,8,8,-8,-10,-9,]),'$end':([1,2,8,9,10,11,14,15,16,17,23,24,25,26,27,29,31,],[0,-7,-16,-14,-11,-3,-13,-4,-5,-6,-15,-12,-1,-2,-8,-10,-9,]),'OR_OP':([1,2,8,9,10,11,14,15,16,17,18,23,24,25,26,27,29,31,],[12,-7,-16,-14,-11,12,-13,-4,-5,-6,12,-15,-12,-1,-2,-8,-10,-9,]),'AND_OP':([1,2,8,9,10,11,14,15,16,17,18,23,24,25,26,27,29,31,],[13,-7,-16,-14,-11,13,-13,-4,-5,-6,13,-15,-12,13,-2,-8,-10,-9,]),'BOOST':([1,2,8,9,10,11,14,15,16,17,18,23,24,25,26,27,29,31,],[14,-7,-16,-14,-11,14,-13,-4,-5,-6,14,-15,-12,14,14,-8,-10,-9,]),'RPAREN':([2,8,9,10,11,14,15,16,17,18,23,24,25,26,27,29,31,],[-7,-16,-14,-11,-3,-13,-4,-5,-6,27,-15,-12,-1,-2,-8,-10,-9,]),'COLUMN':([9,],[22,]),'APPROX':([9,10,],[23,24,]),'RBRACKET':([20,21,30,],[-17,-18,31,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,1,6,11,12,13,18,25,26,],[1,11,18,11,25,26,11,11,11,]),'unary_expression':([0,1,3,4,5,6,11,12,13,18,22,25,26,],[2,2,15,16,17,2,2,2,2,2,29,2,2,]),'phrase_or_term':([7,28,],[19,30,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression OR_OP expression','expression',3,'p_expression_or','parser.py',155),
  ('expression -> expression AND_OP expression','expression',3,'p_expression_and','parser.py',160),
  ('expression -> expression expression','expression',2,'p_expression_implicit','parser.py',165),
  ('unary_expression -> PLUS unary_expression','unary_expression',2,'p_expression_plus','parser.py',170),
  ('unary_expression -> MINUS unary_expression','unary_expression',2,'p_expression_minus','parser.py',175),
  ('unary_expression -> NOT unary_expression','unary_expression',2,'p_expression_not','parser.py',180),
  ('expression -> unary_expression','expression',1,'p_expression_unary','parser.py',185),
  ('unary_expression -> LPAREN expression RPAREN','unary_expression',3,'p_grouping','parser.py',190),
  ('unary_expression -> LBRACKET phrase_or_term TO phrase_or_term RBRACKET','unary_expression',5,'p_range','parser.py',195),
  ('unary_expression -> TERM COLUMN unary_expression','unary_expression',3,'p_field_search','parser.py',202),
  ('unary_expression -> PHRASE','unary_expression',1,'p_quoting','parser.py',210),
  ('unary_expression -> PHRASE APPROX','unary_expression',2,'p_proximity','parser.py',215),
  ('expression -> expression BOOST','expression',2,'p_boosting','parser.py',220),
  ('unary_expression -> TERM','unary_expression',1,'p_terms','parser.py',225),
  ('unary_expression -> TERM APPROX','unary_expression',2,'p_fuzzy','parser.py',230),
  ('unary_expression -> TO','unary_expression',1,'p_to_as_term','parser.py',236),
  ('phrase_or_term -> TERM','phrase_or_term',1,'p_phrase_or_term','parser.py',241),
  ('phrase_or_term -> PHRASE','phrase_or_term',1,'p_phrase_or_term','parser.py',242),
]
