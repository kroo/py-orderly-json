# $ANTLR 3.2 Sep 23, 2009 12:02:23 OrderlyJSON.g 2010-06-22 19:12:37

import sys
from antlr3 import *
from antlr3.compat import set, frozenset


# for convenience in actions
HIDDEN = BaseRecognizer.HIDDEN

# token types
INTEGER=10
T__29=29
T__28=28
T__27=27
T__26=26
T__25=25
T__24=24
T__23=23
ESC=16
T__22=22
PROPERTY_NAME_TOKEN=9
T__21=21
T__20=20
EOF=-1
FRAC=11
T__30=30
QUOTE_OR_BACKSLASH_OR_CONTROL_CHARACTER=14
T__19=19
T__31=31
T__32=32
T__33=33
WS=4
T__34=34
T__18=18
T__35=35
T__17=17
T__36=36
T__37=37
EXP=12
T__38=38
HEX=15
OPTIONAL_ADDITIONAL_MARKER=6
COMMENT=5
OPTIONAL_PERL_REGEX=7
OPTIONAL_OPTIONAL_MARKER=8
STRING=13


class OrderlyJSONLexer(Lexer):

    grammarFileName = "OrderlyJSON.g"
    antlr_version = version_str_to_tuple("3.2 Sep 23, 2009 12:02:23")
    antlr_version_str = "3.2 Sep 23, 2009 12:02:23"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(OrderlyJSONLexer, self).__init__(input, state)


        self.dfa13 = self.DFA13(
            self, 13,
            eot = self.DFA13_eot,
            eof = self.DFA13_eof,
            min = self.DFA13_min,
            max = self.DFA13_max,
            accept = self.DFA13_accept,
            special = self.DFA13_special,
            transition = self.DFA13_transition
            )






    # $ANTLR start "T__17"
    def mT__17(self, ):

        try:
            _type = T__17
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:7:7: ( ';' )
            # OrderlyJSON.g:7:9: ';'
            pass 
            self.match(59)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__17"



    # $ANTLR start "T__18"
    def mT__18(self, ):

        try:
            _type = T__18
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:8:7: ( 'integer' )
            # OrderlyJSON.g:8:9: 'integer'
            pass 
            self.match("integer")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__18"



    # $ANTLR start "T__19"
    def mT__19(self, ):

        try:
            _type = T__19
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:9:7: ( 'number' )
            # OrderlyJSON.g:9:9: 'number'
            pass 
            self.match("number")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__19"



    # $ANTLR start "T__20"
    def mT__20(self, ):

        try:
            _type = T__20
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:10:7: ( 'boolean' )
            # OrderlyJSON.g:10:9: 'boolean'
            pass 
            self.match("boolean")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__20"



    # $ANTLR start "T__21"
    def mT__21(self, ):

        try:
            _type = T__21
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:11:7: ( 'null' )
            # OrderlyJSON.g:11:9: 'null'
            pass 
            self.match("null")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__21"



    # $ANTLR start "T__22"
    def mT__22(self, ):

        try:
            _type = T__22
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:12:7: ( 'any' )
            # OrderlyJSON.g:12:9: 'any'
            pass 
            self.match("any")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__22"



    # $ANTLR start "T__23"
    def mT__23(self, ):

        try:
            _type = T__23
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:13:7: ( 'array' )
            # OrderlyJSON.g:13:9: 'array'
            pass 
            self.match("array")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__23"



    # $ANTLR start "T__24"
    def mT__24(self, ):

        try:
            _type = T__24
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:14:7: ( '{' )
            # OrderlyJSON.g:14:9: '{'
            pass 
            self.match(123)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__24"



    # $ANTLR start "T__25"
    def mT__25(self, ):

        try:
            _type = T__25
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:15:7: ( '}' )
            # OrderlyJSON.g:15:9: '}'
            pass 
            self.match(125)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__25"



    # $ANTLR start "T__26"
    def mT__26(self, ):

        try:
            _type = T__26
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:16:7: ( '[' )
            # OrderlyJSON.g:16:9: '['
            pass 
            self.match(91)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__26"



    # $ANTLR start "T__27"
    def mT__27(self, ):

        try:
            _type = T__27
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:17:7: ( ']' )
            # OrderlyJSON.g:17:9: ']'
            pass 
            self.match(93)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__27"



    # $ANTLR start "T__28"
    def mT__28(self, ):

        try:
            _type = T__28
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:18:7: ( 'object' )
            # OrderlyJSON.g:18:9: 'object'
            pass 
            self.match("object")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__28"



    # $ANTLR start "T__29"
    def mT__29(self, ):

        try:
            _type = T__29
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:19:7: ( 'union' )
            # OrderlyJSON.g:19:9: 'union'
            pass 
            self.match("union")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__29"



    # $ANTLR start "T__30"
    def mT__30(self, ):

        try:
            _type = T__30
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:20:7: ( 'string' )
            # OrderlyJSON.g:20:9: 'string'
            pass 
            self.match("string")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__30"



    # $ANTLR start "T__31"
    def mT__31(self, ):

        try:
            _type = T__31
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:21:7: ( ',' )
            # OrderlyJSON.g:21:9: ','
            pass 
            self.match(44)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__31"



    # $ANTLR start "T__32"
    def mT__32(self, ):

        try:
            _type = T__32
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:22:7: ( '`' )
            # OrderlyJSON.g:22:9: '`'
            pass 
            self.match(96)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__32"



    # $ANTLR start "T__33"
    def mT__33(self, ):

        try:
            _type = T__33
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:23:7: ( '<' )
            # OrderlyJSON.g:23:9: '<'
            pass 
            self.match(60)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__33"



    # $ANTLR start "T__34"
    def mT__34(self, ):

        try:
            _type = T__34
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:24:7: ( '>' )
            # OrderlyJSON.g:24:9: '>'
            pass 
            self.match(62)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__34"



    # $ANTLR start "T__35"
    def mT__35(self, ):

        try:
            _type = T__35
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:25:7: ( '=' )
            # OrderlyJSON.g:25:9: '='
            pass 
            self.match(61)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__35"



    # $ANTLR start "T__36"
    def mT__36(self, ):

        try:
            _type = T__36
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:26:7: ( ':' )
            # OrderlyJSON.g:26:9: ':'
            pass 
            self.match(58)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__36"



    # $ANTLR start "T__37"
    def mT__37(self, ):

        try:
            _type = T__37
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:27:7: ( 'true' )
            # OrderlyJSON.g:27:9: 'true'
            pass 
            self.match("true")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__37"



    # $ANTLR start "T__38"
    def mT__38(self, ):

        try:
            _type = T__38
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:28:7: ( 'false' )
            # OrderlyJSON.g:28:9: 'false'
            pass 
            self.match("false")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__38"



    # $ANTLR start "WS"
    def mWS(self, ):

        try:
            _type = WS
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:29:4: ( ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+ )
            # OrderlyJSON.g:29:6: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            pass 
            # OrderlyJSON.g:29:6: ( '\\t' | ' ' | '\\r' | '\\n' | '\\u000C' )+
            cnt1 = 0
            while True: #loop1
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((9 <= LA1_0 <= 10) or (12 <= LA1_0 <= 13) or LA1_0 == 32) :
                    alt1 = 1


                if alt1 == 1:
                    # OrderlyJSON.g:
                    pass 
                    if (9 <= self.input.LA(1) <= 10) or (12 <= self.input.LA(1) <= 13) or self.input.LA(1) == 32:
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt1 >= 1:
                        break #loop1

                    eee = EarlyExitException(1, self.input)
                    raise eee

                cnt1 += 1
            #action start
            _channel = HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "WS"



    # $ANTLR start "COMMENT"
    def mCOMMENT(self, ):

        try:
            _type = COMMENT
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:31:9: ( ( '//' | '#' ) (~ '\\n' )* )
            # OrderlyJSON.g:31:11: ( '//' | '#' ) (~ '\\n' )*
            pass 
            # OrderlyJSON.g:31:11: ( '//' | '#' )
            alt2 = 2
            LA2_0 = self.input.LA(1)

            if (LA2_0 == 47) :
                alt2 = 1
            elif (LA2_0 == 35) :
                alt2 = 2
            else:
                nvae = NoViableAltException("", 2, 0, self.input)

                raise nvae

            if alt2 == 1:
                # OrderlyJSON.g:31:12: '//'
                pass 
                self.match("//")


            elif alt2 == 2:
                # OrderlyJSON.g:31:19: '#'
                pass 
                self.match(35)



            # OrderlyJSON.g:31:24: (~ '\\n' )*
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if ((0 <= LA3_0 <= 9) or (11 <= LA3_0 <= 65535)) :
                    alt3 = 1


                if alt3 == 1:
                    # OrderlyJSON.g:31:25: ~ '\\n'
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop3
            #action start
            _channel = HIDDEN; 
            #action end



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "COMMENT"



    # $ANTLR start "OPTIONAL_OPTIONAL_MARKER"
    def mOPTIONAL_OPTIONAL_MARKER(self, ):

        try:
            _type = OPTIONAL_OPTIONAL_MARKER
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:104:26: ( '?' )
            # OrderlyJSON.g:104:28: '?'
            pass 
            self.match(63)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OPTIONAL_OPTIONAL_MARKER"



    # $ANTLR start "OPTIONAL_ADDITIONAL_MARKER"
    def mOPTIONAL_ADDITIONAL_MARKER(self, ):

        try:
            _type = OPTIONAL_ADDITIONAL_MARKER
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:106:28: ( '*' )
            # OrderlyJSON.g:106:30: '*'
            pass 
            self.match(42)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OPTIONAL_ADDITIONAL_MARKER"



    # $ANTLR start "PROPERTY_NAME_TOKEN"
    def mPROPERTY_NAME_TOKEN(self, ):

        try:
            _type = PROPERTY_NAME_TOKEN
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:119:21: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '-' )+ )
            # OrderlyJSON.g:119:23: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '-' )+
            pass 
            # OrderlyJSON.g:119:23: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '-' )+
            cnt4 = 0
            while True: #loop4
                alt4 = 2
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 45 or (65 <= LA4_0 <= 90) or LA4_0 == 95 or (97 <= LA4_0 <= 122)) :
                    alt4 = 1


                if alt4 == 1:
                    # OrderlyJSON.g:
                    pass 
                    if self.input.LA(1) == 45 or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "PROPERTY_NAME_TOKEN"



    # $ANTLR start "OPTIONAL_PERL_REGEX"
    def mOPTIONAL_PERL_REGEX(self, ):

        try:
            _type = OPTIONAL_PERL_REGEX
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:121:21: ( ( '/' ( (~ '/' ) | '\\\\/' )+ '/' ) )
            # OrderlyJSON.g:121:23: ( '/' ( (~ '/' ) | '\\\\/' )+ '/' )
            pass 
            # OrderlyJSON.g:121:23: ( '/' ( (~ '/' ) | '\\\\/' )+ '/' )
            # OrderlyJSON.g:121:24: '/' ( (~ '/' ) | '\\\\/' )+ '/'
            pass 
            self.match(47)
            # OrderlyJSON.g:121:28: ( (~ '/' ) | '\\\\/' )+
            cnt5 = 0
            while True: #loop5
                alt5 = 3
                LA5_0 = self.input.LA(1)

                if (LA5_0 == 92) :
                    LA5_2 = self.input.LA(2)

                    if (LA5_2 == 47) :
                        LA5_4 = self.input.LA(3)

                        if ((0 <= LA5_4 <= 65535)) :
                            alt5 = 2

                        else:
                            alt5 = 1


                    elif ((0 <= LA5_2 <= 46) or (48 <= LA5_2 <= 65535)) :
                        alt5 = 1


                elif ((0 <= LA5_0 <= 46) or (48 <= LA5_0 <= 91) or (93 <= LA5_0 <= 65535)) :
                    alt5 = 1


                if alt5 == 1:
                    # OrderlyJSON.g:121:30: (~ '/' )
                    pass 
                    # OrderlyJSON.g:121:30: (~ '/' )
                    # OrderlyJSON.g:121:31: ~ '/'
                    pass 
                    if (0 <= self.input.LA(1) <= 46) or (48 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse






                elif alt5 == 2:
                    # OrderlyJSON.g:121:39: '\\\\/'
                    pass 
                    self.match("\\/")


                else:
                    if cnt5 >= 1:
                        break #loop5

                    eee = EarlyExitException(5, self.input)
                    raise eee

                cnt5 += 1
            self.match(47)






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OPTIONAL_PERL_REGEX"



    # $ANTLR start "QUOTE_OR_BACKSLASH_OR_CONTROL_CHARACTER"
    def mQUOTE_OR_BACKSLASH_OR_CONTROL_CHARACTER(self, ):

        try:
            # OrderlyJSON.g:168:3: ( '\"' | '\\\\' | '\\\\' . )
            alt6 = 3
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 34) :
                alt6 = 1
            elif (LA6_0 == 92) :
                LA6_2 = self.input.LA(2)

                if ((0 <= LA6_2 <= 65535)) :
                    alt6 = 3
                else:
                    alt6 = 2
            else:
                nvae = NoViableAltException("", 6, 0, self.input)

                raise nvae

            if alt6 == 1:
                # OrderlyJSON.g:168:6: '\"'
                pass 
                self.match(34)


            elif alt6 == 2:
                # OrderlyJSON.g:169:6: '\\\\'
                pass 
                self.match(92)


            elif alt6 == 3:
                # OrderlyJSON.g:170:6: '\\\\' .
                pass 
                self.match(92)
                self.matchAny()



        finally:

            pass

    # $ANTLR end "QUOTE_OR_BACKSLASH_OR_CONTROL_CHARACTER"



    # $ANTLR start "STRING"
    def mSTRING(self, ):

        try:
            _type = STRING
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:173:9: ( '\"' (~ '\"' )* '\"' )
            # OrderlyJSON.g:173:12: '\"' (~ '\"' )* '\"'
            pass 
            self.match(34)
            # OrderlyJSON.g:173:16: (~ '\"' )*
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((0 <= LA7_0 <= 33) or (35 <= LA7_0 <= 65535)) :
                    alt7 = 1


                if alt7 == 1:
                    # OrderlyJSON.g:173:16: ~ '\"'
                    pass 
                    if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop7
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "STRING"



    # $ANTLR start "HEX"
    def mHEX(self, ):

        try:
            # OrderlyJSON.g:176:6: ( 'a' .. 'f' | 'A' .. 'F' | '0' .. '9' )
            # OrderlyJSON.g:
            pass 
            if (48 <= self.input.LA(1) <= 57) or (65 <= self.input.LA(1) <= 70) or (97 <= self.input.LA(1) <= 102):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse





        finally:

            pass

    # $ANTLR end "HEX"



    # $ANTLR start "ESC"
    def mESC(self, ):

        try:
            _type = ESC
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:180:5: ( '\\\\\\\\' )
            # OrderlyJSON.g:180:7: '\\\\\\\\'
            pass 
            self.match("\\\\")



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "ESC"



    # $ANTLR start "INTEGER"
    def mINTEGER(self, ):

        try:
            _type = INTEGER
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:182:11: ( ( '-' )? ( '0' .. '9' )+ )
            # OrderlyJSON.g:182:13: ( '-' )? ( '0' .. '9' )+
            pass 
            # OrderlyJSON.g:182:13: ( '-' )?
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if (LA8_0 == 45) :
                alt8 = 1
            if alt8 == 1:
                # OrderlyJSON.g:182:13: '-'
                pass 
                self.match(45)



            # OrderlyJSON.g:182:18: ( '0' .. '9' )+
            cnt9 = 0
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((48 <= LA9_0 <= 57)) :
                    alt9 = 1


                if alt9 == 1:
                    # OrderlyJSON.g:182:19: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt9 >= 1:
                        break #loop9

                    eee = EarlyExitException(9, self.input)
                    raise eee

                cnt9 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "INTEGER"



    # $ANTLR start "EXP"
    def mEXP(self, ):

        try:
            _type = EXP
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:184:6: ( ( 'e' | 'E' ) ( '-' | '+' )? ( '0' .. '9' )+ )
            # OrderlyJSON.g:184:8: ( 'e' | 'E' ) ( '-' | '+' )? ( '0' .. '9' )+
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # OrderlyJSON.g:184:20: ( '-' | '+' )?
            alt10 = 2
            LA10_0 = self.input.LA(1)

            if (LA10_0 == 43 or LA10_0 == 45) :
                alt10 = 1
            if alt10 == 1:
                # OrderlyJSON.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            # OrderlyJSON.g:184:35: ( '0' .. '9' )+
            cnt11 = 0
            while True: #loop11
                alt11 = 2
                LA11_0 = self.input.LA(1)

                if ((48 <= LA11_0 <= 57)) :
                    alt11 = 1


                if alt11 == 1:
                    # OrderlyJSON.g:184:36: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt11 >= 1:
                        break #loop11

                    eee = EarlyExitException(11, self.input)
                    raise eee

                cnt11 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "EXP"



    # $ANTLR start "FRAC"
    def mFRAC(self, ):

        try:
            _type = FRAC
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:186:6: ( '.' ( '0' .. '9' )+ )
            # OrderlyJSON.g:186:8: '.' ( '0' .. '9' )+
            pass 
            self.match(46)
            # OrderlyJSON.g:186:12: ( '0' .. '9' )+
            cnt12 = 0
            while True: #loop12
                alt12 = 2
                LA12_0 = self.input.LA(1)

                if ((48 <= LA12_0 <= 57)) :
                    alt12 = 1


                if alt12 == 1:
                    # OrderlyJSON.g:186:13: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt12 >= 1:
                        break #loop12

                    eee = EarlyExitException(12, self.input)
                    raise eee

                cnt12 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FRAC"



    def mTokens(self):
        # OrderlyJSON.g:1:8: ( T__17 | T__18 | T__19 | T__20 | T__21 | T__22 | T__23 | T__24 | T__25 | T__26 | T__27 | T__28 | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | WS | COMMENT | OPTIONAL_OPTIONAL_MARKER | OPTIONAL_ADDITIONAL_MARKER | PROPERTY_NAME_TOKEN | OPTIONAL_PERL_REGEX | STRING | ESC | INTEGER | EXP | FRAC )
        alt13 = 33
        alt13 = self.dfa13.predict(self.input)
        if alt13 == 1:
            # OrderlyJSON.g:1:10: T__17
            pass 
            self.mT__17()


        elif alt13 == 2:
            # OrderlyJSON.g:1:16: T__18
            pass 
            self.mT__18()


        elif alt13 == 3:
            # OrderlyJSON.g:1:22: T__19
            pass 
            self.mT__19()


        elif alt13 == 4:
            # OrderlyJSON.g:1:28: T__20
            pass 
            self.mT__20()


        elif alt13 == 5:
            # OrderlyJSON.g:1:34: T__21
            pass 
            self.mT__21()


        elif alt13 == 6:
            # OrderlyJSON.g:1:40: T__22
            pass 
            self.mT__22()


        elif alt13 == 7:
            # OrderlyJSON.g:1:46: T__23
            pass 
            self.mT__23()


        elif alt13 == 8:
            # OrderlyJSON.g:1:52: T__24
            pass 
            self.mT__24()


        elif alt13 == 9:
            # OrderlyJSON.g:1:58: T__25
            pass 
            self.mT__25()


        elif alt13 == 10:
            # OrderlyJSON.g:1:64: T__26
            pass 
            self.mT__26()


        elif alt13 == 11:
            # OrderlyJSON.g:1:70: T__27
            pass 
            self.mT__27()


        elif alt13 == 12:
            # OrderlyJSON.g:1:76: T__28
            pass 
            self.mT__28()


        elif alt13 == 13:
            # OrderlyJSON.g:1:82: T__29
            pass 
            self.mT__29()


        elif alt13 == 14:
            # OrderlyJSON.g:1:88: T__30
            pass 
            self.mT__30()


        elif alt13 == 15:
            # OrderlyJSON.g:1:94: T__31
            pass 
            self.mT__31()


        elif alt13 == 16:
            # OrderlyJSON.g:1:100: T__32
            pass 
            self.mT__32()


        elif alt13 == 17:
            # OrderlyJSON.g:1:106: T__33
            pass 
            self.mT__33()


        elif alt13 == 18:
            # OrderlyJSON.g:1:112: T__34
            pass 
            self.mT__34()


        elif alt13 == 19:
            # OrderlyJSON.g:1:118: T__35
            pass 
            self.mT__35()


        elif alt13 == 20:
            # OrderlyJSON.g:1:124: T__36
            pass 
            self.mT__36()


        elif alt13 == 21:
            # OrderlyJSON.g:1:130: T__37
            pass 
            self.mT__37()


        elif alt13 == 22:
            # OrderlyJSON.g:1:136: T__38
            pass 
            self.mT__38()


        elif alt13 == 23:
            # OrderlyJSON.g:1:142: WS
            pass 
            self.mWS()


        elif alt13 == 24:
            # OrderlyJSON.g:1:145: COMMENT
            pass 
            self.mCOMMENT()


        elif alt13 == 25:
            # OrderlyJSON.g:1:153: OPTIONAL_OPTIONAL_MARKER
            pass 
            self.mOPTIONAL_OPTIONAL_MARKER()


        elif alt13 == 26:
            # OrderlyJSON.g:1:178: OPTIONAL_ADDITIONAL_MARKER
            pass 
            self.mOPTIONAL_ADDITIONAL_MARKER()


        elif alt13 == 27:
            # OrderlyJSON.g:1:205: PROPERTY_NAME_TOKEN
            pass 
            self.mPROPERTY_NAME_TOKEN()


        elif alt13 == 28:
            # OrderlyJSON.g:1:225: OPTIONAL_PERL_REGEX
            pass 
            self.mOPTIONAL_PERL_REGEX()


        elif alt13 == 29:
            # OrderlyJSON.g:1:245: STRING
            pass 
            self.mSTRING()


        elif alt13 == 30:
            # OrderlyJSON.g:1:252: ESC
            pass 
            self.mESC()


        elif alt13 == 31:
            # OrderlyJSON.g:1:256: INTEGER
            pass 
            self.mINTEGER()


        elif alt13 == 32:
            # OrderlyJSON.g:1:264: EXP
            pass 
            self.mEXP()


        elif alt13 == 33:
            # OrderlyJSON.g:1:268: FRAC
            pass 
            self.mFRAC()







    # lookup tables for DFA #13

    DFA13_eot = DFA.unpack(
        u"\2\uffff\4\37\4\uffff\3\37\6\uffff\2\37\5\uffff\1\37\2\uffff\1"
        u"\37\3\uffff\12\37\1\uffff\1\37\1\uffff\4\37\1\75\10\37\1\106\1"
        u"\37\1\uffff\4\37\1\114\3\37\1\uffff\1\37\1\121\1\37\1\123\1\37"
        u"\1\uffff\1\125\1\37\1\127\1\37\1\uffff\1\131\1\uffff\1\132\1\uffff"
        u"\1\133\1\uffff\1\134\4\uffff"
        )

    DFA13_eof = DFA.unpack(
        u"\135\uffff"
        )

    DFA13_min = DFA.unpack(
        u"\1\11\1\uffff\1\156\1\165\1\157\1\156\4\uffff\1\142\1\156\1\164"
        u"\6\uffff\1\162\1\141\1\uffff\1\0\3\uffff\1\60\2\uffff\1\53\3\uffff"
        u"\1\164\1\154\1\157\1\171\1\162\1\152\1\151\1\162\1\165\1\154\1"
        u"\uffff\1\60\1\uffff\1\145\1\142\2\154\1\55\1\141\1\145\1\157\1"
        u"\151\1\145\1\163\1\147\1\145\1\55\1\145\1\uffff\1\171\1\143\2\156"
        u"\1\55\2\145\1\162\1\uffff\1\141\1\55\1\164\1\55\1\147\1\uffff\1"
        u"\55\1\162\1\55\1\156\1\uffff\1\55\1\uffff\1\55\1\uffff\1\55\1\uffff"
        u"\1\55\4\uffff"
        )

    DFA13_max = DFA.unpack(
        u"\1\175\1\uffff\1\156\1\165\1\157\1\162\4\uffff\1\142\1\156\1\164"
        u"\6\uffff\1\162\1\141\1\uffff\1\uffff\3\uffff\1\71\2\uffff\1\71"
        u"\3\uffff\1\164\1\155\1\157\1\171\1\162\1\152\1\151\1\162\1\165"
        u"\1\154\1\uffff\1\71\1\uffff\1\145\1\142\2\154\1\172\1\141\1\145"
        u"\1\157\1\151\1\145\1\163\1\147\1\145\1\172\1\145\1\uffff\1\171"
        u"\1\143\2\156\1\172\2\145\1\162\1\uffff\1\141\1\172\1\164\1\172"
        u"\1\147\1\uffff\1\172\1\162\1\172\1\156\1\uffff\1\172\1\uffff\1"
        u"\172\1\uffff\1\172\1\uffff\1\172\4\uffff"
        )

    DFA13_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\10\1\11\1\12\1\13\3\uffff\1\17\1\20\1\21"
        u"\1\22\1\23\1\24\2\uffff\1\27\1\uffff\1\30\1\31\1\32\1\uffff\1\35"
        u"\1\36\1\uffff\1\37\1\33\1\41\12\uffff\1\34\1\uffff\1\40\17\uffff"
        u"\1\6\10\uffff\1\5\5\uffff\1\25\4\uffff\1\7\1\uffff\1\15\1\uffff"
        u"\1\26\1\uffff\1\3\1\uffff\1\14\1\16\1\2\1\4"
        )

    DFA13_special = DFA.unpack(
        u"\26\uffff\1\0\106\uffff"
        )

            
    DFA13_transition = [
        DFA.unpack(u"\2\25\1\uffff\2\25\22\uffff\1\25\1\uffff\1\33\1\27\6"
        u"\uffff\1\31\1\uffff\1\15\1\32\1\40\1\26\12\36\1\22\1\1\1\17\1\21"
        u"\1\20\1\30\1\uffff\4\37\1\35\25\37\1\10\1\34\1\11\1\uffff\1\37"
        u"\1\16\1\5\1\4\2\37\1\35\1\24\2\37\1\2\4\37\1\3\1\12\3\37\1\14\1"
        u"\23\1\13\5\37\1\6\1\uffff\1\7"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\41"),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u"\1\43"),
        DFA.unpack(u"\1\44\3\uffff\1\45"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\46"),
        DFA.unpack(u"\1\47"),
        DFA.unpack(u"\1\50"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\51"),
        DFA.unpack(u"\1\52"),
        DFA.unpack(u""),
        DFA.unpack(u"\57\53\1\27\uffd0\53"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\36"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\55\1\uffff\1\54\2\uffff\12\55"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u"\1\60\1\57"),
        DFA.unpack(u"\1\61"),
        DFA.unpack(u"\1\62"),
        DFA.unpack(u"\1\63"),
        DFA.unpack(u"\1\64"),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u"\1\67"),
        DFA.unpack(u"\1\70"),
        DFA.unpack(u""),
        DFA.unpack(u"\12\55"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\71"),
        DFA.unpack(u"\1\72"),
        DFA.unpack(u"\1\73"),
        DFA.unpack(u"\1\74"),
        DFA.unpack(u"\1\37\23\uffff\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u"\1\76"),
        DFA.unpack(u"\1\77"),
        DFA.unpack(u"\1\100"),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u"\1\102"),
        DFA.unpack(u"\1\103"),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\37\23\uffff\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u"\1\113"),
        DFA.unpack(u"\1\37\23\uffff\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u"\1\117"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\120"),
        DFA.unpack(u"\1\37\23\uffff\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u"\1\37\23\uffff\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\23\uffff\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u"\1\126"),
        DFA.unpack(u"\1\37\23\uffff\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u"\1\130"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\23\uffff\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\23\uffff\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\23\uffff\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\37\23\uffff\32\37\4\uffff\1\37\1\uffff\32\37"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #13

    class DFA13(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA13_22 = input.LA(1)

                s = -1
                if (LA13_22 == 47):
                    s = 23

                elif ((0 <= LA13_22 <= 46) or (48 <= LA13_22 <= 65535)):
                    s = 43

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 13, _s, input)
            self_.error(nvae)
            raise nvae
 



def main(argv, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr):
    from antlr3.main import LexerMain
    main = LexerMain(OrderlyJSONLexer)
    main.stdin = stdin
    main.stdout = stdout
    main.stderr = stderr
    main.execute(argv)


if __name__ == '__main__':
    main(sys.argv)
