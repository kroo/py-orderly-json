# $ANTLR 3.2 Sep 23, 2009 12:02:23 OrderlyJSON.g 2010-06-15 14:20:39

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
CHARACTER=13
FRAC=11
T__30=30
T__19=19
QUOTE_OR_BACKSLASH_OR_CONTROL_CHARACTER=14
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
T__39=39
OPTIONAL_ADDITIONAL_MARKER=6
COMMENT=5
OPTIONAL_PERL_REGEX=7
OPTIONAL_OPTIONAL_MARKER=8


class OrderlyJSONLexer(Lexer):

    grammarFileName = "OrderlyJSON.g"
    antlr_version = version_str_to_tuple("3.2 Sep 23, 2009 12:02:23")
    antlr_version_str = "3.2 Sep 23, 2009 12:02:23"

    def __init__(self, input=None, state=None):
        if state is None:
            state = RecognizerSharedState()
        super(OrderlyJSONLexer, self).__init__(input, state)


        self.dfa11 = self.DFA11(
            self, 11,
            eot = self.DFA11_eot,
            eof = self.DFA11_eof,
            min = self.DFA11_min,
            max = self.DFA11_max,
            accept = self.DFA11_accept,
            special = self.DFA11_special,
            transition = self.DFA11_transition
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



    # $ANTLR start "T__39"
    def mT__39(self, ):

        try:
            _type = T__39
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:29:7: ( '\"' )
            # OrderlyJSON.g:29:9: '\"'
            pass 
            self.match(34)



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "T__39"



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

            # OrderlyJSON.g:31:9: ( '//' (~ '\\n' )* )
            # OrderlyJSON.g:31:11: '//' (~ '\\n' )*
            pass 
            self.match("//")
            # OrderlyJSON.g:31:16: (~ '\\n' )*
            while True: #loop2
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if ((0 <= LA2_0 <= 9) or (11 <= LA2_0 <= 65535)) :
                    alt2 = 1


                if alt2 == 1:
                    # OrderlyJSON.g:31:17: ~ '\\n'
                    pass 
                    if (0 <= self.input.LA(1) <= 9) or (11 <= self.input.LA(1) <= 65535):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    break #loop2
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
            cnt3 = 0
            while True: #loop3
                alt3 = 2
                LA3_0 = self.input.LA(1)

                if (LA3_0 == 45 or (65 <= LA3_0 <= 90) or LA3_0 == 95 or (97 <= LA3_0 <= 122)) :
                    alt3 = 1


                if alt3 == 1:
                    # OrderlyJSON.g:
                    pass 
                    if self.input.LA(1) == 45 or (65 <= self.input.LA(1) <= 90) or self.input.LA(1) == 95 or (97 <= self.input.LA(1) <= 122):
                        self.input.consume()
                    else:
                        mse = MismatchedSetException(None, self.input)
                        self.recover(mse)
                        raise mse



                else:
                    if cnt3 >= 1:
                        break #loop3

                    eee = EarlyExitException(3, self.input)
                    raise eee

                cnt3 += 1



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
            cnt4 = 0
            while True: #loop4
                alt4 = 3
                LA4_0 = self.input.LA(1)

                if (LA4_0 == 92) :
                    LA4_2 = self.input.LA(2)

                    if (LA4_2 == 47) :
                        LA4_4 = self.input.LA(3)

                        if ((0 <= LA4_4 <= 65535)) :
                            alt4 = 2

                        else:
                            alt4 = 1


                    elif ((0 <= LA4_2 <= 46) or (48 <= LA4_2 <= 65535)) :
                        alt4 = 1


                elif ((0 <= LA4_0 <= 46) or (48 <= LA4_0 <= 91) or (93 <= LA4_0 <= 65535)) :
                    alt4 = 1


                if alt4 == 1:
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






                elif alt4 == 2:
                    # OrderlyJSON.g:121:39: '\\\\/'
                    pass 
                    self.match("\\/")


                else:
                    if cnt4 >= 1:
                        break #loop4

                    eee = EarlyExitException(4, self.input)
                    raise eee

                cnt4 += 1
            self.match(47)






            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "OPTIONAL_PERL_REGEX"



    # $ANTLR start "QUOTE_OR_BACKSLASH_OR_CONTROL_CHARACTER"
    def mQUOTE_OR_BACKSLASH_OR_CONTROL_CHARACTER(self, ):

        try:
            # OrderlyJSON.g:170:3: ( '\"' | '\\\\' | '\\\\' . )
            alt5 = 3
            LA5_0 = self.input.LA(1)

            if (LA5_0 == 34) :
                alt5 = 1
            elif (LA5_0 == 92) :
                LA5_2 = self.input.LA(2)

                if ((0 <= LA5_2 <= 65535)) :
                    alt5 = 3
                else:
                    alt5 = 2
            else:
                nvae = NoViableAltException("", 5, 0, self.input)

                raise nvae

            if alt5 == 1:
                # OrderlyJSON.g:170:6: '\"'
                pass 
                self.match(34)


            elif alt5 == 2:
                # OrderlyJSON.g:171:6: '\\\\'
                pass 
                self.match(92)


            elif alt5 == 3:
                # OrderlyJSON.g:172:6: '\\\\' .
                pass 
                self.match(92)
                self.matchAny()



        finally:

            pass

    # $ANTLR end "QUOTE_OR_BACKSLASH_OR_CONTROL_CHARACTER"



    # $ANTLR start "CHARACTER"
    def mCHARACTER(self, ):

        try:
            _type = CHARACTER
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:175:12: (~ '\"' )
            # OrderlyJSON.g:175:15: ~ '\"'
            pass 
            if (0 <= self.input.LA(1) <= 33) or (35 <= self.input.LA(1) <= 65535):
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse




            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "CHARACTER"



    # $ANTLR start "HEX"
    def mHEX(self, ):

        try:
            # OrderlyJSON.g:178:6: ( 'a' .. 'f' | 'A' .. 'F' | '0' .. '9' )
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

            # OrderlyJSON.g:182:5: ( '\\\\\\\\' )
            # OrderlyJSON.g:182:7: '\\\\\\\\'
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

            # OrderlyJSON.g:184:11: ( ( '-' )? ( '0' .. '9' )+ )
            # OrderlyJSON.g:184:13: ( '-' )? ( '0' .. '9' )+
            pass 
            # OrderlyJSON.g:184:13: ( '-' )?
            alt6 = 2
            LA6_0 = self.input.LA(1)

            if (LA6_0 == 45) :
                alt6 = 1
            if alt6 == 1:
                # OrderlyJSON.g:184:13: '-'
                pass 
                self.match(45)



            # OrderlyJSON.g:184:18: ( '0' .. '9' )+
            cnt7 = 0
            while True: #loop7
                alt7 = 2
                LA7_0 = self.input.LA(1)

                if ((48 <= LA7_0 <= 57)) :
                    alt7 = 1


                if alt7 == 1:
                    # OrderlyJSON.g:184:19: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt7 >= 1:
                        break #loop7

                    eee = EarlyExitException(7, self.input)
                    raise eee

                cnt7 += 1



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

            # OrderlyJSON.g:186:6: ( ( 'e' | 'E' ) ( '-' | '+' )? ( '0' .. '9' )+ )
            # OrderlyJSON.g:186:8: ( 'e' | 'E' ) ( '-' | '+' )? ( '0' .. '9' )+
            pass 
            if self.input.LA(1) == 69 or self.input.LA(1) == 101:
                self.input.consume()
            else:
                mse = MismatchedSetException(None, self.input)
                self.recover(mse)
                raise mse

            # OrderlyJSON.g:186:20: ( '-' | '+' )?
            alt8 = 2
            LA8_0 = self.input.LA(1)

            if (LA8_0 == 43 or LA8_0 == 45) :
                alt8 = 1
            if alt8 == 1:
                # OrderlyJSON.g:
                pass 
                if self.input.LA(1) == 43 or self.input.LA(1) == 45:
                    self.input.consume()
                else:
                    mse = MismatchedSetException(None, self.input)
                    self.recover(mse)
                    raise mse




            # OrderlyJSON.g:186:35: ( '0' .. '9' )+
            cnt9 = 0
            while True: #loop9
                alt9 = 2
                LA9_0 = self.input.LA(1)

                if ((48 <= LA9_0 <= 57)) :
                    alt9 = 1


                if alt9 == 1:
                    # OrderlyJSON.g:186:36: '0' .. '9'
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

    # $ANTLR end "EXP"



    # $ANTLR start "FRAC"
    def mFRAC(self, ):

        try:
            _type = FRAC
            _channel = DEFAULT_CHANNEL

            # OrderlyJSON.g:188:6: ( '.' ( '0' .. '9' )+ )
            # OrderlyJSON.g:188:8: '.' ( '0' .. '9' )+
            pass 
            self.match(46)
            # OrderlyJSON.g:188:12: ( '0' .. '9' )+
            cnt10 = 0
            while True: #loop10
                alt10 = 2
                LA10_0 = self.input.LA(1)

                if ((48 <= LA10_0 <= 57)) :
                    alt10 = 1


                if alt10 == 1:
                    # OrderlyJSON.g:188:13: '0' .. '9'
                    pass 
                    self.matchRange(48, 57)


                else:
                    if cnt10 >= 1:
                        break #loop10

                    eee = EarlyExitException(10, self.input)
                    raise eee

                cnt10 += 1



            self._state.type = _type
            self._state.channel = _channel

        finally:

            pass

    # $ANTLR end "FRAC"



    def mTokens(self):
        # OrderlyJSON.g:1:8: ( T__17 | T__18 | T__19 | T__20 | T__21 | T__22 | T__23 | T__24 | T__25 | T__26 | T__27 | T__28 | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | WS | COMMENT | OPTIONAL_OPTIONAL_MARKER | OPTIONAL_ADDITIONAL_MARKER | PROPERTY_NAME_TOKEN | OPTIONAL_PERL_REGEX | CHARACTER | ESC | INTEGER | EXP | FRAC )
        alt11 = 34
        alt11 = self.dfa11.predict(self.input)
        if alt11 == 1:
            # OrderlyJSON.g:1:10: T__17
            pass 
            self.mT__17()


        elif alt11 == 2:
            # OrderlyJSON.g:1:16: T__18
            pass 
            self.mT__18()


        elif alt11 == 3:
            # OrderlyJSON.g:1:22: T__19
            pass 
            self.mT__19()


        elif alt11 == 4:
            # OrderlyJSON.g:1:28: T__20
            pass 
            self.mT__20()


        elif alt11 == 5:
            # OrderlyJSON.g:1:34: T__21
            pass 
            self.mT__21()


        elif alt11 == 6:
            # OrderlyJSON.g:1:40: T__22
            pass 
            self.mT__22()


        elif alt11 == 7:
            # OrderlyJSON.g:1:46: T__23
            pass 
            self.mT__23()


        elif alt11 == 8:
            # OrderlyJSON.g:1:52: T__24
            pass 
            self.mT__24()


        elif alt11 == 9:
            # OrderlyJSON.g:1:58: T__25
            pass 
            self.mT__25()


        elif alt11 == 10:
            # OrderlyJSON.g:1:64: T__26
            pass 
            self.mT__26()


        elif alt11 == 11:
            # OrderlyJSON.g:1:70: T__27
            pass 
            self.mT__27()


        elif alt11 == 12:
            # OrderlyJSON.g:1:76: T__28
            pass 
            self.mT__28()


        elif alt11 == 13:
            # OrderlyJSON.g:1:82: T__29
            pass 
            self.mT__29()


        elif alt11 == 14:
            # OrderlyJSON.g:1:88: T__30
            pass 
            self.mT__30()


        elif alt11 == 15:
            # OrderlyJSON.g:1:94: T__31
            pass 
            self.mT__31()


        elif alt11 == 16:
            # OrderlyJSON.g:1:100: T__32
            pass 
            self.mT__32()


        elif alt11 == 17:
            # OrderlyJSON.g:1:106: T__33
            pass 
            self.mT__33()


        elif alt11 == 18:
            # OrderlyJSON.g:1:112: T__34
            pass 
            self.mT__34()


        elif alt11 == 19:
            # OrderlyJSON.g:1:118: T__35
            pass 
            self.mT__35()


        elif alt11 == 20:
            # OrderlyJSON.g:1:124: T__36
            pass 
            self.mT__36()


        elif alt11 == 21:
            # OrderlyJSON.g:1:130: T__37
            pass 
            self.mT__37()


        elif alt11 == 22:
            # OrderlyJSON.g:1:136: T__38
            pass 
            self.mT__38()


        elif alt11 == 23:
            # OrderlyJSON.g:1:142: T__39
            pass 
            self.mT__39()


        elif alt11 == 24:
            # OrderlyJSON.g:1:148: WS
            pass 
            self.mWS()


        elif alt11 == 25:
            # OrderlyJSON.g:1:151: COMMENT
            pass 
            self.mCOMMENT()


        elif alt11 == 26:
            # OrderlyJSON.g:1:159: OPTIONAL_OPTIONAL_MARKER
            pass 
            self.mOPTIONAL_OPTIONAL_MARKER()


        elif alt11 == 27:
            # OrderlyJSON.g:1:184: OPTIONAL_ADDITIONAL_MARKER
            pass 
            self.mOPTIONAL_ADDITIONAL_MARKER()


        elif alt11 == 28:
            # OrderlyJSON.g:1:211: PROPERTY_NAME_TOKEN
            pass 
            self.mPROPERTY_NAME_TOKEN()


        elif alt11 == 29:
            # OrderlyJSON.g:1:231: OPTIONAL_PERL_REGEX
            pass 
            self.mOPTIONAL_PERL_REGEX()


        elif alt11 == 30:
            # OrderlyJSON.g:1:251: CHARACTER
            pass 
            self.mCHARACTER()


        elif alt11 == 31:
            # OrderlyJSON.g:1:261: ESC
            pass 
            self.mESC()


        elif alt11 == 32:
            # OrderlyJSON.g:1:265: INTEGER
            pass 
            self.mINTEGER()


        elif alt11 == 33:
            # OrderlyJSON.g:1:273: EXP
            pass 
            self.mEXP()


        elif alt11 == 34:
            # OrderlyJSON.g:1:277: FRAC
            pass 
            self.mFRAC()







    # lookup tables for DFA #11

    DFA11_eot = DFA.unpack(
        u"\2\uffff\4\43\4\uffff\3\43\6\uffff\2\43\2\uffff\1\40\2\uffff\1"
        u"\43\2\40\1\43\1\40\3\uffff\1\43\1\uffff\4\43\4\uffff\3\43\6\uffff"
        u"\2\43\7\uffff\1\43\2\uffff\4\43\1\120\10\43\1\131\1\43\1\uffff"
        u"\4\43\1\137\3\43\1\uffff\1\43\1\144\1\43\1\146\1\43\1\uffff\1\150"
        u"\1\43\1\152\1\43\1\uffff\1\154\1\uffff\1\155\1\uffff\1\156\1\uffff"
        u"\1\157\4\uffff"
        )

    DFA11_eof = DFA.unpack(
        u"\160\uffff"
        )

    DFA11_min = DFA.unpack(
        u"\1\0\1\uffff\1\156\1\165\1\157\1\156\4\uffff\1\142\1\156\1\164"
        u"\6\uffff\1\162\1\141\2\uffff\1\0\2\uffff\1\60\1\134\1\60\1\53\1"
        u"\60\3\uffff\1\164\1\uffff\1\154\1\157\1\171\1\162\4\uffff\1\152"
        u"\1\151\1\162\6\uffff\1\165\1\154\7\uffff\1\60\2\uffff\1\145\1\142"
        u"\2\154\1\55\1\141\1\145\1\157\1\151\1\145\1\163\1\147\1\145\1\55"
        u"\1\145\1\uffff\1\171\1\143\2\156\1\55\2\145\1\162\1\uffff\1\141"
        u"\1\55\1\164\1\55\1\147\1\uffff\1\55\1\162\1\55\1\156\1\uffff\1"
        u"\55\1\uffff\1\55\1\uffff\1\55\1\uffff\1\55\4\uffff"
        )

    DFA11_max = DFA.unpack(
        u"\1\uffff\1\uffff\1\156\1\165\1\157\1\162\4\uffff\1\142\1\156\1"
        u"\164\6\uffff\1\162\1\141\2\uffff\1\uffff\2\uffff\1\71\1\134\3\71"
        u"\3\uffff\1\164\1\uffff\1\155\1\157\1\171\1\162\4\uffff\1\152\1"
        u"\151\1\162\6\uffff\1\165\1\154\7\uffff\1\71\2\uffff\1\145\1\142"
        u"\2\154\1\172\1\141\1\145\1\157\1\151\1\145\1\163\1\147\1\145\1"
        u"\172\1\145\1\uffff\1\171\1\143\2\156\1\172\2\145\1\162\1\uffff"
        u"\1\141\1\172\1\164\1\172\1\147\1\uffff\1\172\1\162\1\172\1\156"
        u"\1\uffff\1\172\1\uffff\1\172\1\uffff\1\172\1\uffff\1\172\4\uffff"
        )

    DFA11_accept = DFA.unpack(
        u"\1\uffff\1\1\4\uffff\1\10\1\11\1\12\1\13\3\uffff\1\17\1\20\1\21"
        u"\1\22\1\23\1\24\2\uffff\1\27\1\30\1\uffff\1\32\1\33\5\uffff\1\34"
        u"\1\36\1\1\1\uffff\1\34\4\uffff\1\10\1\11\1\12\1\13\3\uffff\1\17"
        u"\1\20\1\21\1\22\1\23\1\24\2\uffff\1\30\1\31\1\35\1\32\1\33\1\40"
        u"\1\37\1\uffff\1\41\1\42\17\uffff\1\6\10\uffff\1\5\5\uffff\1\25"
        u"\4\uffff\1\7\1\uffff\1\15\1\uffff\1\26\1\uffff\1\3\1\uffff\1\14"
        u"\1\16\1\2\1\4"
        )

    DFA11_special = DFA.unpack(
        u"\1\1\26\uffff\1\0\130\uffff"
        )

            
    DFA11_transition = [
        DFA.unpack(u"\11\40\2\26\1\40\2\26\22\40\1\26\1\40\1\25\7\40\1\31"
        u"\1\40\1\15\1\32\1\36\1\27\12\34\1\22\1\1\1\17\1\21\1\20\1\30\1"
        u"\40\4\37\1\35\25\37\1\10\1\33\1\11\1\40\1\37\1\16\1\5\1\4\2\37"
        u"\1\35\1\24\2\37\1\2\4\37\1\3\1\12\3\37\1\14\1\23\1\13\5\37\1\6"
        u"\1\40\1\7\uff82\40"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\42"),
        DFA.unpack(u"\1\44"),
        DFA.unpack(u"\1\45"),
        DFA.unpack(u"\1\46\3\uffff\1\47"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\54"),
        DFA.unpack(u"\1\55"),
        DFA.unpack(u"\1\56"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\65"),
        DFA.unpack(u"\1\66"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\57\71\1\70\uffd0\71"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\74"),
        DFA.unpack(u"\1\75"),
        DFA.unpack(u"\12\74"),
        DFA.unpack(u"\1\77\1\uffff\1\76\2\uffff\12\77"),
        DFA.unpack(u"\12\100"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\101"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\103\1\102"),
        DFA.unpack(u"\1\104"),
        DFA.unpack(u"\1\105"),
        DFA.unpack(u"\1\106"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\107"),
        DFA.unpack(u"\1\110"),
        DFA.unpack(u"\1\111"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\112"),
        DFA.unpack(u"\1\113"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\12\77"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"\1\114"),
        DFA.unpack(u"\1\115"),
        DFA.unpack(u"\1\116"),
        DFA.unpack(u"\1\117"),
        DFA.unpack(u"\1\43\23\uffff\32\43\4\uffff\1\43\1\uffff\32\43"),
        DFA.unpack(u"\1\121"),
        DFA.unpack(u"\1\122"),
        DFA.unpack(u"\1\123"),
        DFA.unpack(u"\1\124"),
        DFA.unpack(u"\1\125"),
        DFA.unpack(u"\1\126"),
        DFA.unpack(u"\1\127"),
        DFA.unpack(u"\1\130"),
        DFA.unpack(u"\1\43\23\uffff\32\43\4\uffff\1\43\1\uffff\32\43"),
        DFA.unpack(u"\1\132"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\133"),
        DFA.unpack(u"\1\134"),
        DFA.unpack(u"\1\135"),
        DFA.unpack(u"\1\136"),
        DFA.unpack(u"\1\43\23\uffff\32\43\4\uffff\1\43\1\uffff\32\43"),
        DFA.unpack(u"\1\140"),
        DFA.unpack(u"\1\141"),
        DFA.unpack(u"\1\142"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\143"),
        DFA.unpack(u"\1\43\23\uffff\32\43\4\uffff\1\43\1\uffff\32\43"),
        DFA.unpack(u"\1\145"),
        DFA.unpack(u"\1\43\23\uffff\32\43\4\uffff\1\43\1\uffff\32\43"),
        DFA.unpack(u"\1\147"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\23\uffff\32\43\4\uffff\1\43\1\uffff\32\43"),
        DFA.unpack(u"\1\151"),
        DFA.unpack(u"\1\43\23\uffff\32\43\4\uffff\1\43\1\uffff\32\43"),
        DFA.unpack(u"\1\153"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\23\uffff\32\43\4\uffff\1\43\1\uffff\32\43"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\23\uffff\32\43\4\uffff\1\43\1\uffff\32\43"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\23\uffff\32\43\4\uffff\1\43\1\uffff\32\43"),
        DFA.unpack(u""),
        DFA.unpack(u"\1\43\23\uffff\32\43\4\uffff\1\43\1\uffff\32\43"),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u""),
        DFA.unpack(u"")
    ]

    # class definition for DFA #11

    class DFA11(DFA):
        pass


        def specialStateTransition(self_, s, input):
            # convince pylint that my self_ magic is ok ;)
            # pylint: disable-msg=E0213

            # pretend we are a member of the recognizer
            # thus semantic predicates can be evaluated
            self = self_.recognizer

            _s = s

            if s == 0: 
                LA11_23 = input.LA(1)

                s = -1
                if (LA11_23 == 47):
                    s = 56

                elif ((0 <= LA11_23 <= 46) or (48 <= LA11_23 <= 65535)):
                    s = 57

                else:
                    s = 32

                if s >= 0:
                    return s
            elif s == 1: 
                LA11_0 = input.LA(1)

                s = -1
                if (LA11_0 == 59):
                    s = 1

                elif (LA11_0 == 105):
                    s = 2

                elif (LA11_0 == 110):
                    s = 3

                elif (LA11_0 == 98):
                    s = 4

                elif (LA11_0 == 97):
                    s = 5

                elif (LA11_0 == 123):
                    s = 6

                elif (LA11_0 == 125):
                    s = 7

                elif (LA11_0 == 91):
                    s = 8

                elif (LA11_0 == 93):
                    s = 9

                elif (LA11_0 == 111):
                    s = 10

                elif (LA11_0 == 117):
                    s = 11

                elif (LA11_0 == 115):
                    s = 12

                elif (LA11_0 == 44):
                    s = 13

                elif (LA11_0 == 96):
                    s = 14

                elif (LA11_0 == 60):
                    s = 15

                elif (LA11_0 == 62):
                    s = 16

                elif (LA11_0 == 61):
                    s = 17

                elif (LA11_0 == 58):
                    s = 18

                elif (LA11_0 == 116):
                    s = 19

                elif (LA11_0 == 102):
                    s = 20

                elif (LA11_0 == 34):
                    s = 21

                elif ((9 <= LA11_0 <= 10) or (12 <= LA11_0 <= 13) or LA11_0 == 32):
                    s = 22

                elif (LA11_0 == 47):
                    s = 23

                elif (LA11_0 == 63):
                    s = 24

                elif (LA11_0 == 42):
                    s = 25

                elif (LA11_0 == 45):
                    s = 26

                elif (LA11_0 == 92):
                    s = 27

                elif ((48 <= LA11_0 <= 57)):
                    s = 28

                elif (LA11_0 == 69 or LA11_0 == 101):
                    s = 29

                elif (LA11_0 == 46):
                    s = 30

                elif ((65 <= LA11_0 <= 68) or (70 <= LA11_0 <= 90) or LA11_0 == 95 or (99 <= LA11_0 <= 100) or (103 <= LA11_0 <= 104) or (106 <= LA11_0 <= 109) or (112 <= LA11_0 <= 114) or (118 <= LA11_0 <= 122)):
                    s = 31

                elif ((0 <= LA11_0 <= 8) or LA11_0 == 11 or (14 <= LA11_0 <= 31) or LA11_0 == 33 or (35 <= LA11_0 <= 41) or LA11_0 == 43 or LA11_0 == 64 or LA11_0 == 94 or LA11_0 == 124 or (126 <= LA11_0 <= 65535)):
                    s = 32

                if s >= 0:
                    return s

            nvae = NoViableAltException(self_.getDescription(), 11, _s, input)
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
