# Generated from gram.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("\\\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\5\2\23\n\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7")
        buf.write("\3\34\n\3\f\3\16\3\37\13\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4")
        buf.write("\'\n\4\f\4\16\4*\13\4\3\4\3\4\3\5\3\5\7\5\60\n\5\f\5\16")
        buf.write("\5\63\13\5\3\6\3\6\5\6\67\n\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\7\7E\n\7\f\7\16\7H\13\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\7\bU\n\b\f\b\16")
        buf.write("\bX\13\b\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\2\2[\2\20")
        buf.write("\3\2\2\2\4\27\3\2\2\2\6\"\3\2\2\2\b-\3\2\2\2\n\66\3\2")
        buf.write("\2\2\f8\3\2\2\2\16K\3\2\2\2\20\22\5\4\3\2\21\23\5\6\4")
        buf.write("\2\22\21\3\2\2\2\22\23\3\2\2\2\23\24\3\2\2\2\24\25\5\b")
        buf.write("\5\2\25\26\7\2\2\3\26\3\3\2\2\2\27\30\7\3\2\2\30\35\7")
        buf.write("\16\2\2\31\32\7\t\2\2\32\34\7\16\2\2\33\31\3\2\2\2\34")
        buf.write("\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36 \3\2\2\2\37")
        buf.write("\35\3\2\2\2 !\7\b\2\2!\5\3\2\2\2\"#\7\4\2\2#(\7\16\2\2")
        buf.write("$%\7\t\2\2%\'\7\16\2\2&$\3\2\2\2\'*\3\2\2\2(&\3\2\2\2")
        buf.write("()\3\2\2\2)+\3\2\2\2*(\3\2\2\2+,\7\b\2\2,\7\3\2\2\2-\61")
        buf.write("\5\n\6\2.\60\5\n\6\2/.\3\2\2\2\60\63\3\2\2\2\61/\3\2\2")
        buf.write("\2\61\62\3\2\2\2\62\t\3\2\2\2\63\61\3\2\2\2\64\67\5\f")
        buf.write("\7\2\65\67\5\16\b\2\66\64\3\2\2\2\66\65\3\2\2\2\67\13")
        buf.write("\3\2\2\289\7\16\2\29:\7\13\2\2:;\7\16\2\2;<\7\f\2\2<=")
        buf.write("\7\7\2\2=>\7\r\2\2>?\7\6\2\2?F\7\16\2\2@A\7\n\2\2AB\7")
        buf.write("\r\2\2BC\7\6\2\2CE\7\16\2\2D@\3\2\2\2EH\3\2\2\2FD\3\2")
        buf.write("\2\2FG\3\2\2\2GI\3\2\2\2HF\3\2\2\2IJ\7\b\2\2J\r\3\2\2")
        buf.write("\2KL\7\16\2\2LM\7\7\2\2MN\7\r\2\2NO\7\6\2\2OV\7\16\2\2")
        buf.write("PQ\7\n\2\2QR\7\r\2\2RS\7\6\2\2SU\7\16\2\2TP\3\2\2\2UX")
        buf.write("\3\2\2\2VT\3\2\2\2VW\3\2\2\2WY\3\2\2\2XV\3\2\2\2YZ\7\b")
        buf.write("\2\2Z\17\3\2\2\2\t\22\35(\61\66FV")
        return buf.getvalue()


class gramParser ( Parser ):

    grammarFileName = "gram.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'States'", "'Actions'", "'transition'", 
                     "':'", "'->'", "';'", "','", "'+'", "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "STATES", "ACTIONS", "TRANSITION", "DPOINT", 
                      "FLECHE", "SEMI", "VIRG", "PLUS", "LCROCH", "RCROCH", 
                      "INT", "ID", "WS" ]

    RULE_program = 0
    RULE_defstates = 1
    RULE_defactions = 2
    RULE_transitions = 3
    RULE_trans = 4
    RULE_transact = 5
    RULE_transnoact = 6

    ruleNames =  [ "program", "defstates", "defactions", "transitions", 
                   "trans", "transact", "transnoact" ]

    EOF = Token.EOF
    STATES=1
    ACTIONS=2
    TRANSITION=3
    DPOINT=4
    FLECHE=5
    SEMI=6
    VIRG=7
    PLUS=8
    LCROCH=9
    RCROCH=10
    INT=11
    ID=12
    WS=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def defstates(self):
            return self.getTypedRuleContext(gramParser.DefstatesContext,0)


        def transitions(self):
            return self.getTypedRuleContext(gramParser.TransitionsContext,0)


        def EOF(self):
            return self.getToken(gramParser.EOF, 0)

        def defactions(self):
            return self.getTypedRuleContext(gramParser.DefactionsContext,0)


        def getRuleIndex(self):
            return gramParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = gramParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.defstates()
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==gramParser.ACTIONS:
                self.state = 15
                self.defactions()


            self.state = 18
            self.transitions()
            self.state = 19
            self.match(gramParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DefstatesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATES(self):
            return self.getToken(gramParser.STATES, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def SEMI(self):
            return self.getToken(gramParser.SEMI, 0)

        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.VIRG)
            else:
                return self.getToken(gramParser.VIRG, i)

        def getRuleIndex(self):
            return gramParser.RULE_defstates

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefstates" ):
                listener.enterDefstates(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefstates" ):
                listener.exitDefstates(self)




    def defstates(self):

        localctx = gramParser.DefstatesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_defstates)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(gramParser.STATES)
            self.state = 22
            self.match(gramParser.ID)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==gramParser.VIRG:
                self.state = 23
                self.match(gramParser.VIRG)
                self.state = 24
                self.match(gramParser.ID)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
            self.match(gramParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DefactionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTIONS(self):
            return self.getToken(gramParser.ACTIONS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def SEMI(self):
            return self.getToken(gramParser.SEMI, 0)

        def VIRG(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.VIRG)
            else:
                return self.getToken(gramParser.VIRG, i)

        def getRuleIndex(self):
            return gramParser.RULE_defactions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefactions" ):
                listener.enterDefactions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefactions" ):
                listener.exitDefactions(self)




    def defactions(self):

        localctx = gramParser.DefactionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_defactions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(gramParser.ACTIONS)
            self.state = 33
            self.match(gramParser.ID)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==gramParser.VIRG:
                self.state = 34
                self.match(gramParser.VIRG)
                self.state = 35
                self.match(gramParser.ID)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(gramParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TransitionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def trans(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramParser.TransContext)
            else:
                return self.getTypedRuleContext(gramParser.TransContext,i)


        def getRuleIndex(self):
            return gramParser.RULE_transitions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransitions" ):
                listener.enterTransitions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransitions" ):
                listener.exitTransitions(self)




    def transitions(self):

        localctx = gramParser.TransitionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_transitions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.trans()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==gramParser.ID:
                self.state = 44
                self.trans()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TransContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def transact(self):
            return self.getTypedRuleContext(gramParser.TransactContext,0)


        def transnoact(self):
            return self.getTypedRuleContext(gramParser.TransnoactContext,0)


        def getRuleIndex(self):
            return gramParser.RULE_trans

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrans" ):
                listener.enterTrans(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrans" ):
                listener.exitTrans(self)




    def trans(self):

        localctx = gramParser.TransContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_trans)
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.transact()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.transnoact()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TransactContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def LCROCH(self):
            return self.getToken(gramParser.LCROCH, 0)

        def RCROCH(self):
            return self.getToken(gramParser.RCROCH, 0)

        def FLECHE(self):
            return self.getToken(gramParser.FLECHE, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.INT)
            else:
                return self.getToken(gramParser.INT, i)

        def DPOINT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.DPOINT)
            else:
                return self.getToken(gramParser.DPOINT, i)

        def SEMI(self):
            return self.getToken(gramParser.SEMI, 0)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.PLUS)
            else:
                return self.getToken(gramParser.PLUS, i)

        def getRuleIndex(self):
            return gramParser.RULE_transact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransact" ):
                listener.enterTransact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransact" ):
                listener.exitTransact(self)




    def transact(self):

        localctx = gramParser.TransactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_transact)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(gramParser.ID)
            self.state = 55
            self.match(gramParser.LCROCH)
            self.state = 56
            self.match(gramParser.ID)
            self.state = 57
            self.match(gramParser.RCROCH)
            self.state = 58
            self.match(gramParser.FLECHE)
            self.state = 59
            self.match(gramParser.INT)
            self.state = 60
            self.match(gramParser.DPOINT)
            self.state = 61
            self.match(gramParser.ID)
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==gramParser.PLUS:
                self.state = 62
                self.match(gramParser.PLUS)
                self.state = 63
                self.match(gramParser.INT)
                self.state = 64
                self.match(gramParser.DPOINT)
                self.state = 65
                self.match(gramParser.ID)
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 71
            self.match(gramParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TransnoactContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.ID)
            else:
                return self.getToken(gramParser.ID, i)

        def FLECHE(self):
            return self.getToken(gramParser.FLECHE, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.INT)
            else:
                return self.getToken(gramParser.INT, i)

        def DPOINT(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.DPOINT)
            else:
                return self.getToken(gramParser.DPOINT, i)

        def SEMI(self):
            return self.getToken(gramParser.SEMI, 0)

        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(gramParser.PLUS)
            else:
                return self.getToken(gramParser.PLUS, i)

        def getRuleIndex(self):
            return gramParser.RULE_transnoact

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransnoact" ):
                listener.enterTransnoact(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransnoact" ):
                listener.exitTransnoact(self)




    def transnoact(self):

        localctx = gramParser.TransnoactContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_transnoact)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(gramParser.ID)
            self.state = 74
            self.match(gramParser.FLECHE)
            self.state = 75
            self.match(gramParser.INT)
            self.state = 76
            self.match(gramParser.DPOINT)
            self.state = 77
            self.match(gramParser.ID)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==gramParser.PLUS:
                self.state = 78
                self.match(gramParser.PLUS)
                self.state = 79
                self.match(gramParser.INT)
                self.state = 80
                self.match(gramParser.DPOINT)
                self.state = 81
                self.match(gramParser.ID)
                self.state = 86
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 87
            self.match(gramParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





