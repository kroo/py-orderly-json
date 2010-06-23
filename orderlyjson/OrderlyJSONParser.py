# $ANTLR 3.2 Sep 23, 2009 12:02:23 OrderlyJSON.g 2010-06-22 19:12:36

import sys
from antlr3 import *
from antlr3.compat import set, frozenset
         
import sys
import traceback
from orderly_json import Prefix, Entry, Suffix

from OrderlyJSONLexer import OrderlyJSONLexer



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
QUOTE_OR_BACKSLASH_OR_CONTROL_CHARACTER=14
T__19=19
T__30=30
T__31=31
T__32=32
WS=4
T__33=33
T__34=34
T__35=35
T__18=18
T__36=36
T__17=17
EXP=12
T__37=37
HEX=15
T__38=38
OPTIONAL_ADDITIONAL_MARKER=6
COMMENT=5
STRING=13
OPTIONAL_OPTIONAL_MARKER=8
OPTIONAL_PERL_REGEX=7

# token names
tokenNames = [
    "<invalid>", "<EOR>", "<DOWN>", "<UP>", 
    "WS", "COMMENT", "OPTIONAL_ADDITIONAL_MARKER", "OPTIONAL_PERL_REGEX", 
    "OPTIONAL_OPTIONAL_MARKER", "PROPERTY_NAME_TOKEN", "INTEGER", "FRAC", 
    "EXP", "STRING", "QUOTE_OR_BACKSLASH_OR_CONTROL_CHARACTER", "HEX", "ESC", 
    "';'", "'integer'", "'number'", "'boolean'", "'null'", "'any'", "'array'", 
    "'{'", "'}'", "'['", "']'", "'object'", "'union'", "'string'", "','", 
    "'`'", "'<'", "'>'", "'='", "':'", "'true'", "'false'"
]




class OrderlyJSONParser(Parser):
    grammarFileName = "OrderlyJSON.g"
    antlr_version = version_str_to_tuple("3.2 Sep 23, 2009 12:02:23")
    antlr_version_str = "3.2 Sep 23, 2009 12:02:23"
    tokenNames = tokenNames

    def __init__(self, input, state=None, *args, **kwargs):
        if state is None:
            state = RecognizerSharedState()

        super(OrderlyJSONParser, self).__init__(input, state, *args, **kwargs)






                


        



    # $ANTLR start "orderly_schema"
    # OrderlyJSON.g:33:1: orderly_schema returns [result] : (e= unnamed_entries )? ( ';' )? ;
    def orderly_schema(self, ):

        result = None

        e = None


        try:
            try:
                # OrderlyJSON.g:33:33: ( (e= unnamed_entries )? ( ';' )? )
                # OrderlyJSON.g:33:35: (e= unnamed_entries )? ( ';' )?
                pass 
                # OrderlyJSON.g:33:36: (e= unnamed_entries )?
                alt1 = 2
                LA1_0 = self.input.LA(1)

                if ((18 <= LA1_0 <= 23) or (28 <= LA1_0 <= 30)) :
                    alt1 = 1
                if alt1 == 1:
                    # OrderlyJSON.g:33:36: e= unnamed_entries
                    pass 
                    self._state.following.append(self.FOLLOW_unnamed_entries_in_orderly_schema97)
                    e = self.unnamed_entries()

                    self._state.following.pop()



                # OrderlyJSON.g:33:54: ( ';' )?
                alt2 = 2
                LA2_0 = self.input.LA(1)

                if (LA2_0 == 17) :
                    alt2 = 1
                if alt2 == 1:
                    # OrderlyJSON.g:33:54: ';'
                    pass 
                    self.match(self.input, 17, self.FOLLOW_17_in_orderly_schema100)



                #action start
                result = e
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "orderly_schema"


    # $ANTLR start "named_entries"
    # OrderlyJSON.g:35:1: named_entries returns [result] : e= named_entry ( ';' e2= named_entry )* ;
    def named_entries(self, ):

        result = None

        e = None

        e2 = None


               
        result = []

        try:
            try:
                # OrderlyJSON.g:38:2: (e= named_entry ( ';' e2= named_entry )* )
                # OrderlyJSON.g:39:3: e= named_entry ( ';' e2= named_entry )*
                pass 
                self._state.following.append(self.FOLLOW_named_entry_in_named_entries123)
                e = self.named_entry()

                self._state.following.pop()
                # OrderlyJSON.g:39:17: ( ';' e2= named_entry )*
                while True: #loop3
                    alt3 = 2
                    LA3_0 = self.input.LA(1)

                    if (LA3_0 == 17) :
                        LA3_1 = self.input.LA(2)

                        if ((18 <= LA3_1 <= 23) or (28 <= LA3_1 <= 30)) :
                            alt3 = 1




                    if alt3 == 1:
                        # OrderlyJSON.g:40:5: ';' e2= named_entry
                        pass 
                        self.match(self.input, 17, self.FOLLOW_17_in_named_entries131)
                        self._state.following.append(self.FOLLOW_named_entry_in_named_entries135)
                        e2 = self.named_entry()

                        self._state.following.pop()
                        #action start
                        result.append(e2) 
                        #action end


                    else:
                        break #loop3
                #action start
                result = [e] + result 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "named_entries"


    # $ANTLR start "unnamed_entries"
    # OrderlyJSON.g:43:1: unnamed_entries returns [result] : e= unnamed_entry ( ';' e2= unnamed_entry )* ;
    def unnamed_entries(self, ):

        result = None

        e = None

        e2 = None


               
        result = [];

        try:
            try:
                # OrderlyJSON.g:46:2: (e= unnamed_entry ( ';' e2= unnamed_entry )* )
                # OrderlyJSON.g:47:3: e= unnamed_entry ( ';' e2= unnamed_entry )*
                pass 
                self._state.following.append(self.FOLLOW_unnamed_entry_in_unnamed_entries164)
                e = self.unnamed_entry()

                self._state.following.pop()
                # OrderlyJSON.g:47:19: ( ';' e2= unnamed_entry )*
                while True: #loop4
                    alt4 = 2
                    LA4_0 = self.input.LA(1)

                    if (LA4_0 == 17) :
                        LA4_1 = self.input.LA(2)

                        if ((18 <= LA4_1 <= 23) or (28 <= LA4_1 <= 30)) :
                            alt4 = 1




                    if alt4 == 1:
                        # OrderlyJSON.g:48:6: ';' e2= unnamed_entry
                        pass 
                        self.match(self.input, 17, self.FOLLOW_17_in_unnamed_entries173)
                        self._state.following.append(self.FOLLOW_unnamed_entry_in_unnamed_entries177)
                        e2 = self.unnamed_entry()

                        self._state.following.pop()
                        #action start
                        result.append(e2); 
                        #action end


                    else:
                        break #loop4
                #action start
                result = [e] + result 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "unnamed_entries"


    # $ANTLR start "named_entry"
    # OrderlyJSON.g:51:1: named_entry returns [result] : ( (pref= definition_prefix name= property_name suff= definition_suffix ) | (pref= string_prefix name= property_name suff= string_suffix ) );
    def named_entry(self, ):

        result = None

        pref = None

        name = None

        suff = None


        try:
            try:
                # OrderlyJSON.g:52:3: ( (pref= definition_prefix name= property_name suff= definition_suffix ) | (pref= string_prefix name= property_name suff= string_suffix ) )
                alt5 = 2
                LA5_0 = self.input.LA(1)

                if ((18 <= LA5_0 <= 23) or (28 <= LA5_0 <= 29)) :
                    alt5 = 1
                elif (LA5_0 == 30) :
                    alt5 = 2
                else:
                    nvae = NoViableAltException("", 5, 0, self.input)

                    raise nvae

                if alt5 == 1:
                    # OrderlyJSON.g:52:6: (pref= definition_prefix name= property_name suff= definition_suffix )
                    pass 
                    # OrderlyJSON.g:52:6: (pref= definition_prefix name= property_name suff= definition_suffix )
                    # OrderlyJSON.g:52:7: pref= definition_prefix name= property_name suff= definition_suffix
                    pass 
                    self._state.following.append(self.FOLLOW_definition_prefix_in_named_entry204)
                    pref = self.definition_prefix()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_property_name_in_named_entry208)
                    name = self.property_name()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_definition_suffix_in_named_entry212)
                    suff = self.definition_suffix()

                    self._state.following.pop()



                    #action start
                    result = Entry(pref, name, suff); 
                    #action end


                elif alt5 == 2:
                    # OrderlyJSON.g:53:6: (pref= string_prefix name= property_name suff= string_suffix )
                    pass 
                    # OrderlyJSON.g:53:6: (pref= string_prefix name= property_name suff= string_suffix )
                    # OrderlyJSON.g:53:7: pref= string_prefix name= property_name suff= string_suffix
                    pass 
                    self._state.following.append(self.FOLLOW_string_prefix_in_named_entry225)
                    pref = self.string_prefix()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_property_name_in_named_entry229)
                    name = self.property_name()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_string_suffix_in_named_entry233)
                    suff = self.string_suffix()

                    self._state.following.pop()



                    #action start
                    result = Entry(pref, name, suff); 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "named_entry"


    # $ANTLR start "unnamed_entry"
    # OrderlyJSON.g:56:1: unnamed_entry returns [result] : (pref= definition_prefix suff= definition_suffix | pref= string_prefix suff= string_suffix );
    def unnamed_entry(self, ):

        result = None

        pref = None

        suff = None


        try:
            try:
                # OrderlyJSON.g:57:3: (pref= definition_prefix suff= definition_suffix | pref= string_prefix suff= string_suffix )
                alt6 = 2
                LA6_0 = self.input.LA(1)

                if ((18 <= LA6_0 <= 23) or (28 <= LA6_0 <= 29)) :
                    alt6 = 1
                elif (LA6_0 == 30) :
                    alt6 = 2
                else:
                    nvae = NoViableAltException("", 6, 0, self.input)

                    raise nvae

                if alt6 == 1:
                    # OrderlyJSON.g:57:6: pref= definition_prefix suff= definition_suffix
                    pass 
                    self._state.following.append(self.FOLLOW_definition_prefix_in_unnamed_entry264)
                    pref = self.definition_prefix()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_definition_suffix_in_unnamed_entry268)
                    suff = self.definition_suffix()

                    self._state.following.pop()
                    #action start
                    result = Entry(pref, None, suff) 
                    #action end


                elif alt6 == 2:
                    # OrderlyJSON.g:58:6: pref= string_prefix suff= string_suffix
                    pass 
                    self._state.following.append(self.FOLLOW_string_prefix_in_unnamed_entry280)
                    pref = self.string_prefix()

                    self._state.following.pop()
                    self._state.following.append(self.FOLLOW_string_suffix_in_unnamed_entry284)
                    suff = self.string_suffix()

                    self._state.following.pop()
                    #action start
                    result = Entry(pref, None, suff) 
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "unnamed_entry"


    # $ANTLR start "definition_prefix"
    # OrderlyJSON.g:61:1: definition_prefix returns [result] : ( 'integer' (rng= optional_range )? | 'number' (rng= optional_range )? | 'boolean' | 'null' | 'any' | 'array' ( ( '{' (e= unnamed_entries )? ( ';' )? '}' (o= OPTIONAL_ADDITIONAL_MARKER )? (rng= optional_range )? ) | ( '[' (e= unnamed_entry )? ( ';' )? ']' (rng= optional_range )? ) ) | 'object' '{' (e= named_entries )? ( ';' )? '}' (o= OPTIONAL_ADDITIONAL_MARKER )? | 'union' '{' (e= unnamed_entries )? ( ';' )? '}' );
    def definition_prefix(self, ):

        result = None

        o = None
        rng = None

        e = None


        try:
            try:
                # OrderlyJSON.g:62:3: ( 'integer' (rng= optional_range )? | 'number' (rng= optional_range )? | 'boolean' | 'null' | 'any' | 'array' ( ( '{' (e= unnamed_entries )? ( ';' )? '}' (o= OPTIONAL_ADDITIONAL_MARKER )? (rng= optional_range )? ) | ( '[' (e= unnamed_entry )? ( ';' )? ']' (rng= optional_range )? ) ) | 'object' '{' (e= named_entries )? ( ';' )? '}' (o= OPTIONAL_ADDITIONAL_MARKER )? | 'union' '{' (e= unnamed_entries )? ( ';' )? '}' )
                alt22 = 8
                LA22 = self.input.LA(1)
                if LA22 == 18:
                    alt22 = 1
                elif LA22 == 19:
                    alt22 = 2
                elif LA22 == 20:
                    alt22 = 3
                elif LA22 == 21:
                    alt22 = 4
                elif LA22 == 22:
                    alt22 = 5
                elif LA22 == 23:
                    alt22 = 6
                elif LA22 == 28:
                    alt22 = 7
                elif LA22 == 29:
                    alt22 = 8
                else:
                    nvae = NoViableAltException("", 22, 0, self.input)

                    raise nvae

                if alt22 == 1:
                    # OrderlyJSON.g:62:6: 'integer' (rng= optional_range )?
                    pass 
                    self.match(self.input, 18, self.FOLLOW_18_in_definition_prefix313)
                    # OrderlyJSON.g:62:19: (rng= optional_range )?
                    alt7 = 2
                    LA7_0 = self.input.LA(1)

                    if (LA7_0 == 24) :
                        alt7 = 1
                    if alt7 == 1:
                        # OrderlyJSON.g:62:19: rng= optional_range
                        pass 
                        self._state.following.append(self.FOLLOW_optional_range_in_definition_prefix317)
                        rng = self.optional_range()

                        self._state.following.pop()



                    #action start
                    result = Prefix('integer', rng=('rng' in locals() and rng)) 
                    #action end


                elif alt22 == 2:
                    # OrderlyJSON.g:63:6: 'number' (rng= optional_range )?
                    pass 
                    self.match(self.input, 19, self.FOLLOW_19_in_definition_prefix386)
                    # OrderlyJSON.g:63:18: (rng= optional_range )?
                    alt8 = 2
                    LA8_0 = self.input.LA(1)

                    if (LA8_0 == 24) :
                        alt8 = 1
                    if alt8 == 1:
                        # OrderlyJSON.g:63:18: rng= optional_range
                        pass 
                        self._state.following.append(self.FOLLOW_optional_range_in_definition_prefix390)
                        rng = self.optional_range()

                        self._state.following.pop()



                    #action start
                    result = Prefix('number', rng=('rng' in locals() and rng))  
                    #action end


                elif alt22 == 3:
                    # OrderlyJSON.g:64:6: 'boolean'
                    pass 
                    self.match(self.input, 20, self.FOLLOW_20_in_definition_prefix460)
                    #action start
                    result = Prefix('boolean')
                    #action end


                elif alt22 == 4:
                    # OrderlyJSON.g:65:6: 'null'
                    pass 
                    self.match(self.input, 21, self.FOLLOW_21_in_definition_prefix548)
                    #action start
                    result = Prefix('null')
                    #action end


                elif alt22 == 5:
                    # OrderlyJSON.g:66:6: 'any'
                    pass 
                    self.match(self.input, 22, self.FOLLOW_22_in_definition_prefix639)
                    #action start
                    result = Prefix('any')
                    #action end


                elif alt22 == 6:
                    # OrderlyJSON.g:67:6: 'array' ( ( '{' (e= unnamed_entries )? ( ';' )? '}' (o= OPTIONAL_ADDITIONAL_MARKER )? (rng= optional_range )? ) | ( '[' (e= unnamed_entry )? ( ';' )? ']' (rng= optional_range )? ) )
                    pass 
                    self.match(self.input, 23, self.FOLLOW_23_in_definition_prefix731)
                    # OrderlyJSON.g:67:14: ( ( '{' (e= unnamed_entries )? ( ';' )? '}' (o= OPTIONAL_ADDITIONAL_MARKER )? (rng= optional_range )? ) | ( '[' (e= unnamed_entry )? ( ';' )? ']' (rng= optional_range )? ) )
                    alt16 = 2
                    LA16_0 = self.input.LA(1)

                    if (LA16_0 == 24) :
                        alt16 = 1
                    elif (LA16_0 == 26) :
                        alt16 = 2
                    else:
                        nvae = NoViableAltException("", 16, 0, self.input)

                        raise nvae

                    if alt16 == 1:
                        # OrderlyJSON.g:68:7: ( '{' (e= unnamed_entries )? ( ';' )? '}' (o= OPTIONAL_ADDITIONAL_MARKER )? (rng= optional_range )? )
                        pass 
                        # OrderlyJSON.g:68:7: ( '{' (e= unnamed_entries )? ( ';' )? '}' (o= OPTIONAL_ADDITIONAL_MARKER )? (rng= optional_range )? )
                        # OrderlyJSON.g:68:8: '{' (e= unnamed_entries )? ( ';' )? '}' (o= OPTIONAL_ADDITIONAL_MARKER )? (rng= optional_range )?
                        pass 
                        self.match(self.input, 24, self.FOLLOW_24_in_definition_prefix742)
                        # OrderlyJSON.g:68:13: (e= unnamed_entries )?
                        alt9 = 2
                        LA9_0 = self.input.LA(1)

                        if ((18 <= LA9_0 <= 23) or (28 <= LA9_0 <= 30)) :
                            alt9 = 1
                        if alt9 == 1:
                            # OrderlyJSON.g:68:13: e= unnamed_entries
                            pass 
                            self._state.following.append(self.FOLLOW_unnamed_entries_in_definition_prefix746)
                            e = self.unnamed_entries()

                            self._state.following.pop()



                        # OrderlyJSON.g:68:31: ( ';' )?
                        alt10 = 2
                        LA10_0 = self.input.LA(1)

                        if (LA10_0 == 17) :
                            alt10 = 1
                        if alt10 == 1:
                            # OrderlyJSON.g:68:31: ';'
                            pass 
                            self.match(self.input, 17, self.FOLLOW_17_in_definition_prefix749)



                        self.match(self.input, 25, self.FOLLOW_25_in_definition_prefix752)
                        # OrderlyJSON.g:68:41: (o= OPTIONAL_ADDITIONAL_MARKER )?
                        alt11 = 2
                        LA11_0 = self.input.LA(1)

                        if (LA11_0 == OPTIONAL_ADDITIONAL_MARKER) :
                            alt11 = 1
                        if alt11 == 1:
                            # OrderlyJSON.g:68:41: o= OPTIONAL_ADDITIONAL_MARKER
                            pass 
                            o=self.match(self.input, OPTIONAL_ADDITIONAL_MARKER, self.FOLLOW_OPTIONAL_ADDITIONAL_MARKER_in_definition_prefix756)



                        # OrderlyJSON.g:68:73: (rng= optional_range )?
                        alt12 = 2
                        LA12_0 = self.input.LA(1)

                        if (LA12_0 == 24) :
                            alt12 = 1
                        if alt12 == 1:
                            # OrderlyJSON.g:68:73: rng= optional_range
                            pass 
                            self._state.following.append(self.FOLLOW_optional_range_in_definition_prefix761)
                            rng = self.optional_range()

                            self._state.following.pop()






                        #action start
                        result = Prefix('array', entries=('e' in locals() and e), more=('o' in locals() and o), rng=('rng' in locals() and rng))
                        #action end


                    elif alt16 == 2:
                        # OrderlyJSON.g:69:7: ( '[' (e= unnamed_entry )? ( ';' )? ']' (rng= optional_range )? )
                        pass 
                        # OrderlyJSON.g:69:7: ( '[' (e= unnamed_entry )? ( ';' )? ']' (rng= optional_range )? )
                        # OrderlyJSON.g:69:8: '[' (e= unnamed_entry )? ( ';' )? ']' (rng= optional_range )?
                        pass 
                        self.match(self.input, 26, self.FOLLOW_26_in_definition_prefix778)
                        # OrderlyJSON.g:69:13: (e= unnamed_entry )?
                        alt13 = 2
                        LA13_0 = self.input.LA(1)

                        if ((18 <= LA13_0 <= 23) or (28 <= LA13_0 <= 30)) :
                            alt13 = 1
                        if alt13 == 1:
                            # OrderlyJSON.g:69:13: e= unnamed_entry
                            pass 
                            self._state.following.append(self.FOLLOW_unnamed_entry_in_definition_prefix782)
                            e = self.unnamed_entry()

                            self._state.following.pop()



                        # OrderlyJSON.g:69:29: ( ';' )?
                        alt14 = 2
                        LA14_0 = self.input.LA(1)

                        if (LA14_0 == 17) :
                            alt14 = 1
                        if alt14 == 1:
                            # OrderlyJSON.g:69:29: ';'
                            pass 
                            self.match(self.input, 17, self.FOLLOW_17_in_definition_prefix785)



                        self.match(self.input, 27, self.FOLLOW_27_in_definition_prefix788)
                        # OrderlyJSON.g:69:41: (rng= optional_range )?
                        alt15 = 2
                        LA15_0 = self.input.LA(1)

                        if (LA15_0 == 24) :
                            alt15 = 1
                        if alt15 == 1:
                            # OrderlyJSON.g:69:41: rng= optional_range
                            pass 
                            self._state.following.append(self.FOLLOW_optional_range_in_definition_prefix792)
                            rng = self.optional_range()

                            self._state.following.pop()









                    #action start
                    result = Prefix('array', entries=('e' in locals() and e), rng=('rng' in locals() and rng))
                    #action end


                elif alt22 == 7:
                    # OrderlyJSON.g:70:6: 'object' '{' (e= named_entries )? ( ';' )? '}' (o= OPTIONAL_ADDITIONAL_MARKER )?
                    pass 
                    self.match(self.input, 28, self.FOLLOW_28_in_definition_prefix844)
                    self.match(self.input, 24, self.FOLLOW_24_in_definition_prefix846)
                    # OrderlyJSON.g:70:20: (e= named_entries )?
                    alt17 = 2
                    LA17_0 = self.input.LA(1)

                    if ((18 <= LA17_0 <= 23) or (28 <= LA17_0 <= 30)) :
                        alt17 = 1
                    if alt17 == 1:
                        # OrderlyJSON.g:70:20: e= named_entries
                        pass 
                        self._state.following.append(self.FOLLOW_named_entries_in_definition_prefix850)
                        e = self.named_entries()

                        self._state.following.pop()



                    # OrderlyJSON.g:70:36: ( ';' )?
                    alt18 = 2
                    LA18_0 = self.input.LA(1)

                    if (LA18_0 == 17) :
                        alt18 = 1
                    if alt18 == 1:
                        # OrderlyJSON.g:70:36: ';'
                        pass 
                        self.match(self.input, 17, self.FOLLOW_17_in_definition_prefix853)



                    self.match(self.input, 25, self.FOLLOW_25_in_definition_prefix856)
                    # OrderlyJSON.g:70:46: (o= OPTIONAL_ADDITIONAL_MARKER )?
                    alt19 = 2
                    LA19_0 = self.input.LA(1)

                    if (LA19_0 == OPTIONAL_ADDITIONAL_MARKER) :
                        alt19 = 1
                    if alt19 == 1:
                        # OrderlyJSON.g:70:46: o= OPTIONAL_ADDITIONAL_MARKER
                        pass 
                        o=self.match(self.input, OPTIONAL_ADDITIONAL_MARKER, self.FOLLOW_OPTIONAL_ADDITIONAL_MARKER_in_definition_prefix860)



                    #action start
                    result = Prefix('object', entries=('e' in locals() and e), more=('o' in locals() and o))
                    #action end


                elif alt22 == 8:
                    # OrderlyJSON.g:71:6: 'union' '{' (e= unnamed_entries )? ( ';' )? '}'
                    pass 
                    self.match(self.input, 29, self.FOLLOW_29_in_definition_prefix890)
                    self.match(self.input, 24, self.FOLLOW_24_in_definition_prefix893)
                    # OrderlyJSON.g:71:20: (e= unnamed_entries )?
                    alt20 = 2
                    LA20_0 = self.input.LA(1)

                    if ((18 <= LA20_0 <= 23) or (28 <= LA20_0 <= 30)) :
                        alt20 = 1
                    if alt20 == 1:
                        # OrderlyJSON.g:71:20: e= unnamed_entries
                        pass 
                        self._state.following.append(self.FOLLOW_unnamed_entries_in_definition_prefix897)
                        e = self.unnamed_entries()

                        self._state.following.pop()



                    # OrderlyJSON.g:71:38: ( ';' )?
                    alt21 = 2
                    LA21_0 = self.input.LA(1)

                    if (LA21_0 == 17) :
                        alt21 = 1
                    if alt21 == 1:
                        # OrderlyJSON.g:71:38: ';'
                        pass 
                        self.match(self.input, 17, self.FOLLOW_17_in_definition_prefix900)



                    self.match(self.input, 25, self.FOLLOW_25_in_definition_prefix903)
                    #action start
                    result = Prefix('union', entries=('e' in locals() and e))
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "definition_prefix"


    # $ANTLR start "string_prefix"
    # OrderlyJSON.g:74:1: string_prefix returns [result] : 'string' (rng= optional_range )? ;
    def string_prefix(self, ):

        result = None

        rng = None


        try:
            try:
                # OrderlyJSON.g:74:32: ( 'string' (rng= optional_range )? )
                # OrderlyJSON.g:74:35: 'string' (rng= optional_range )?
                pass 
                self.match(self.input, 30, self.FOLLOW_30_in_string_prefix969)
                # OrderlyJSON.g:74:47: (rng= optional_range )?
                alt23 = 2
                LA23_0 = self.input.LA(1)

                if (LA23_0 == 24) :
                    alt23 = 1
                if alt23 == 1:
                    # OrderlyJSON.g:74:47: rng= optional_range
                    pass 
                    self._state.following.append(self.FOLLOW_optional_range_in_string_prefix973)
                    rng = self.optional_range()

                    self._state.following.pop()



                #action start
                result = Prefix('string', rng=('rng' in locals() and rng))
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "string_prefix"


    # $ANTLR start "string_suffix"
    # OrderlyJSON.g:76:1: string_suffix returns [result] : (regex= OPTIONAL_PERL_REGEX )? suff= definition_suffix ;
    def string_suffix(self, ):

        result = None

        regex = None
        suff = None


        try:
            try:
                # OrderlyJSON.g:76:32: ( (regex= OPTIONAL_PERL_REGEX )? suff= definition_suffix )
                # OrderlyJSON.g:76:35: (regex= OPTIONAL_PERL_REGEX )? suff= definition_suffix
                pass 
                # OrderlyJSON.g:76:40: (regex= OPTIONAL_PERL_REGEX )?
                alt24 = 2
                LA24_0 = self.input.LA(1)

                if (LA24_0 == OPTIONAL_PERL_REGEX) :
                    alt24 = 1
                if alt24 == 1:
                    # OrderlyJSON.g:76:40: regex= OPTIONAL_PERL_REGEX
                    pass 
                    regex=self.match(self.input, OPTIONAL_PERL_REGEX, self.FOLLOW_OPTIONAL_PERL_REGEX_in_string_suffix991)



                self._state.following.append(self.FOLLOW_definition_suffix_in_string_suffix996)
                suff = self.definition_suffix()

                self._state.following.pop()
                #action start
                suff.regex = regex and regex.text; result = suff 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "string_suffix"


    # $ANTLR start "definition_suffix"
    # OrderlyJSON.g:78:1: definition_suffix returns [result] : (enums= optional_enum_values )? (d= optional_default_value )? (requires= optional_requires )? (optional= OPTIONAL_OPTIONAL_MARKER )? (extra= optional_extra_properties )? ;
    def definition_suffix(self, ):

        result = None

        optional = None
        enums = None

        d = None

        requires = None

        extra = None


        try:
            try:
                # OrderlyJSON.g:78:35: ( (enums= optional_enum_values )? (d= optional_default_value )? (requires= optional_requires )? (optional= OPTIONAL_OPTIONAL_MARKER )? (extra= optional_extra_properties )? )
                # OrderlyJSON.g:79:2: (enums= optional_enum_values )? (d= optional_default_value )? (requires= optional_requires )? (optional= OPTIONAL_OPTIONAL_MARKER )? (extra= optional_extra_properties )?
                pass 
                # OrderlyJSON.g:79:7: (enums= optional_enum_values )?
                alt25 = 2
                LA25_0 = self.input.LA(1)

                if (LA25_0 == 26) :
                    alt25 = 1
                if alt25 == 1:
                    # OrderlyJSON.g:79:7: enums= optional_enum_values
                    pass 
                    self._state.following.append(self.FOLLOW_optional_enum_values_in_definition_suffix1012)
                    enums = self.optional_enum_values()

                    self._state.following.pop()



                # OrderlyJSON.g:80:3: (d= optional_default_value )?
                alt26 = 2
                LA26_0 = self.input.LA(1)

                if (LA26_0 == 35) :
                    alt26 = 1
                if alt26 == 1:
                    # OrderlyJSON.g:80:3: d= optional_default_value
                    pass 
                    self._state.following.append(self.FOLLOW_optional_default_value_in_definition_suffix1018)
                    d = self.optional_default_value()

                    self._state.following.pop()



                # OrderlyJSON.g:81:10: (requires= optional_requires )?
                alt27 = 2
                LA27_0 = self.input.LA(1)

                if (LA27_0 == 33) :
                    alt27 = 1
                if alt27 == 1:
                    # OrderlyJSON.g:81:10: requires= optional_requires
                    pass 
                    self._state.following.append(self.FOLLOW_optional_requires_in_definition_suffix1024)
                    requires = self.optional_requires()

                    self._state.following.pop()



                # OrderlyJSON.g:82:10: (optional= OPTIONAL_OPTIONAL_MARKER )?
                alt28 = 2
                LA28_0 = self.input.LA(1)

                if (LA28_0 == OPTIONAL_OPTIONAL_MARKER) :
                    alt28 = 1
                if alt28 == 1:
                    # OrderlyJSON.g:82:10: optional= OPTIONAL_OPTIONAL_MARKER
                    pass 
                    optional=self.match(self.input, OPTIONAL_OPTIONAL_MARKER, self.FOLLOW_OPTIONAL_OPTIONAL_MARKER_in_definition_suffix1030)



                # OrderlyJSON.g:83:7: (extra= optional_extra_properties )?
                alt29 = 2
                LA29_0 = self.input.LA(1)

                if (LA29_0 == 32) :
                    alt29 = 1
                if alt29 == 1:
                    # OrderlyJSON.g:83:7: extra= optional_extra_properties
                    pass 
                    self._state.following.append(self.FOLLOW_optional_extra_properties_in_definition_suffix1036)
                    extra = self.optional_extra_properties()

                    self._state.following.pop()



                #action start
                                                   
                result = Suffix(
                    enums=('enums' in locals() and enums),
                    default_val=('d' in locals() and d),
                    requires=('requires' in locals() and requires),
                    optional=(('optional' in locals()) and optional),
                    extra=('extra' in locals() and extra))
                  
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "definition_suffix"


    # $ANTLR start "csv_property_names"
    # OrderlyJSON.g:92:1: csv_property_names returns [result] : prop= property_name ( ',' prop2= property_name )* ;
    def csv_property_names(self, ):

        result = None

        prop = None

        prop2 = None


               
        result = [];

        try:
            try:
                # OrderlyJSON.g:95:3: (prop= property_name ( ',' prop2= property_name )* )
                # OrderlyJSON.g:96:5: prop= property_name ( ',' prop2= property_name )*
                pass 
                self._state.following.append(self.FOLLOW_property_name_in_csv_property_names1062)
                prop = self.property_name()

                self._state.following.pop()
                # OrderlyJSON.g:96:24: ( ',' prop2= property_name )*
                while True: #loop30
                    alt30 = 2
                    LA30_0 = self.input.LA(1)

                    if (LA30_0 == 31) :
                        alt30 = 1


                    if alt30 == 1:
                        # OrderlyJSON.g:97:7: ',' prop2= property_name
                        pass 
                        self.match(self.input, 31, self.FOLLOW_31_in_csv_property_names1072)
                        self._state.following.append(self.FOLLOW_property_name_in_csv_property_names1076)
                        prop2 = self.property_name()

                        self._state.following.pop()
                        #action start
                        result.append(prop2) 
                        #action end


                    else:
                        break #loop30
                #action start
                result = [prop] + result 
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "csv_property_names"


    # $ANTLR start "optional_extra_properties"
    # OrderlyJSON.g:100:1: optional_extra_properties returns [result] : ( '`' obj= json_object '`' ) ;
    def optional_extra_properties(self, ):

        result = None

        obj = None


        try:
            try:
                # OrderlyJSON.g:100:45: ( ( '`' obj= json_object '`' ) )
                # OrderlyJSON.g:100:48: ( '`' obj= json_object '`' )
                pass 
                # OrderlyJSON.g:100:48: ( '`' obj= json_object '`' )
                # OrderlyJSON.g:100:49: '`' obj= json_object '`'
                pass 
                self.match(self.input, 32, self.FOLLOW_32_in_optional_extra_properties1113)
                self._state.following.append(self.FOLLOW_json_object_in_optional_extra_properties1117)
                obj = self.json_object()

                self._state.following.pop()
                self.match(self.input, 32, self.FOLLOW_32_in_optional_extra_properties1119)



                #action start
                result=obj
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "optional_extra_properties"


    # $ANTLR start "optional_requires"
    # OrderlyJSON.g:102:1: optional_requires returns [result] : ( '<' p= csv_property_names '>' ) ;
    def optional_requires(self, ):

        result = None

        p = None


        try:
            try:
                # OrderlyJSON.g:102:37: ( ( '<' p= csv_property_names '>' ) )
                # OrderlyJSON.g:102:40: ( '<' p= csv_property_names '>' )
                pass 
                # OrderlyJSON.g:102:40: ( '<' p= csv_property_names '>' )
                # OrderlyJSON.g:102:41: '<' p= csv_property_names '>'
                pass 
                self.match(self.input, 33, self.FOLLOW_33_in_optional_requires1137)
                self._state.following.append(self.FOLLOW_csv_property_names_in_optional_requires1141)
                p = self.csv_property_names()

                self._state.following.pop()
                self.match(self.input, 34, self.FOLLOW_34_in_optional_requires1143)



                #action start
                result=p
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "optional_requires"


    # $ANTLR start "optional_enum_values"
    # OrderlyJSON.g:108:1: optional_enum_values returns [result] : arr= json_array ;
    def optional_enum_values(self, ):

        result = None

        arr = None


        try:
            try:
                # OrderlyJSON.g:108:39: (arr= json_array )
                # OrderlyJSON.g:108:41: arr= json_array
                pass 
                self._state.following.append(self.FOLLOW_json_array_in_optional_enum_values1178)
                arr = self.json_array()

                self._state.following.pop()
                #action start
                result = arr
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "optional_enum_values"


    # $ANTLR start "optional_default_value"
    # OrderlyJSON.g:110:1: optional_default_value returns [result] : ( '=' d= json_value ) ;
    def optional_default_value(self, ):

        result = None

        d = None


        try:
            try:
                # OrderlyJSON.g:110:41: ( ( '=' d= json_value ) )
                # OrderlyJSON.g:110:43: ( '=' d= json_value )
                pass 
                # OrderlyJSON.g:110:43: ( '=' d= json_value )
                # OrderlyJSON.g:110:44: '=' d= json_value
                pass 
                self.match(self.input, 35, self.FOLLOW_35_in_optional_default_value1193)
                self._state.following.append(self.FOLLOW_json_value_in_optional_default_value1197)
                d = self.json_value()

                self._state.following.pop()



                #action start
                result=d
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "optional_default_value"


    # $ANTLR start "optional_range"
    # OrderlyJSON.g:112:1: optional_range returns [out] : '{' (s= json_number )? ',' (e= json_number )? '}' ;
    def optional_range(self, ):

        out = None

        s = None

        e = None


        try:
            try:
                # OrderlyJSON.g:112:30: ( '{' (s= json_number )? ',' (e= json_number )? '}' )
                # OrderlyJSON.g:112:32: '{' (s= json_number )? ',' (e= json_number )? '}'
                pass 
                self.match(self.input, 24, self.FOLLOW_24_in_optional_range1212)
                # OrderlyJSON.g:112:37: (s= json_number )?
                alt31 = 2
                LA31_0 = self.input.LA(1)

                if (LA31_0 == INTEGER) :
                    alt31 = 1
                if alt31 == 1:
                    # OrderlyJSON.g:112:37: s= json_number
                    pass 
                    self._state.following.append(self.FOLLOW_json_number_in_optional_range1216)
                    s = self.json_number()

                    self._state.following.pop()



                self.match(self.input, 31, self.FOLLOW_31_in_optional_range1219)
                # OrderlyJSON.g:112:56: (e= json_number )?
                alt32 = 2
                LA32_0 = self.input.LA(1)

                if (LA32_0 == INTEGER) :
                    alt32 = 1
                if alt32 == 1:
                    # OrderlyJSON.g:112:56: e= json_number
                    pass 
                    self._state.following.append(self.FOLLOW_json_number_in_optional_range1223)
                    e = self.json_number()

                    self._state.following.pop()



                self.match(self.input, 25, self.FOLLOW_25_in_optional_range1226)
                #action start
                out = (s, e)
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return out

    # $ANTLR end "optional_range"


    # $ANTLR start "property_name"
    # OrderlyJSON.g:114:1: property_name returns [result] : (s= json_string | r= PROPERTY_NAME_TOKEN );
    def property_name(self, ):

        result = None

        r = None
        s = None


        try:
            try:
                # OrderlyJSON.g:115:3: (s= json_string | r= PROPERTY_NAME_TOKEN )
                alt33 = 2
                LA33_0 = self.input.LA(1)

                if (LA33_0 == STRING) :
                    alt33 = 1
                elif (LA33_0 == PROPERTY_NAME_TOKEN) :
                    alt33 = 2
                else:
                    nvae = NoViableAltException("", 33, 0, self.input)

                    raise nvae

                if alt33 == 1:
                    # OrderlyJSON.g:115:5: s= json_string
                    pass 
                    self._state.following.append(self.FOLLOW_json_string_in_property_name1244)
                    s = self.json_string()

                    self._state.following.pop()
                    #action start
                    result = s
                    #action end


                elif alt33 == 2:
                    # OrderlyJSON.g:116:5: r= PROPERTY_NAME_TOKEN
                    pass 
                    r=self.match(self.input, PROPERTY_NAME_TOKEN, self.FOLLOW_PROPERTY_NAME_TOKEN_in_property_name1282)
                    #action start
                    result = r.text
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "property_name"


    # $ANTLR start "json_object"
    # OrderlyJSON.g:125:1: json_object returns [result] : '{' (m= members )? '}' ;
    def json_object(self, ):

        result = None

        m = None


        try:
            try:
                # OrderlyJSON.g:125:30: ( '{' (m= members )? '}' )
                # OrderlyJSON.g:125:33: '{' (m= members )? '}'
                pass 
                self.match(self.input, 24, self.FOLLOW_24_in_json_object1380)
                # OrderlyJSON.g:125:38: (m= members )?
                alt34 = 2
                LA34_0 = self.input.LA(1)

                if (LA34_0 == STRING) :
                    alt34 = 1
                if alt34 == 1:
                    # OrderlyJSON.g:125:38: m= members
                    pass 
                    self._state.following.append(self.FOLLOW_members_in_json_object1384)
                    m = self.members()

                    self._state.following.pop()



                self.match(self.input, 25, self.FOLLOW_25_in_json_object1387)
                #action start
                result = m or {}
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "json_object"


    # $ANTLR start "members"
    # OrderlyJSON.g:127:1: members returns [d] : p1= pair ( ',' p2= pair )* ;
    def members(self, ):

        d = None

        p1 = None

        p2 = None


               
        d = dict()

        try:
            try:
                # OrderlyJSON.g:131:1: (p1= pair ( ',' p2= pair )* )
                # OrderlyJSON.g:131:4: p1= pair ( ',' p2= pair )*
                pass 
                self._state.following.append(self.FOLLOW_pair_in_members1410)
                p1 = self.pair()

                self._state.following.pop()
                # OrderlyJSON.g:131:12: ( ',' p2= pair )*
                while True: #loop35
                    alt35 = 2
                    LA35_0 = self.input.LA(1)

                    if (LA35_0 == 31) :
                        alt35 = 1


                    if alt35 == 1:
                        # OrderlyJSON.g:132:3: ',' p2= pair
                        pass 
                        self.match(self.input, 31, self.FOLLOW_31_in_members1416)
                        self._state.following.append(self.FOLLOW_pair_in_members1420)
                        p2 = self.pair()

                        self._state.following.pop()
                        #action start
                        d[p2[0]] = p2[1] 
                        #action end


                    else:
                        break #loop35
                #action start
                if not p1[0] in d: d[p1[0]] = p1[1]
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return d

    # $ANTLR end "members"


    # $ANTLR start "pair"
    # OrderlyJSON.g:135:1: pair returns [out] : k= json_string ':' v= json_value ;
    def pair(self, ):

        out = None

        k = None

        v = None


        try:
            try:
                # OrderlyJSON.g:135:20: (k= json_string ':' v= json_value )
                # OrderlyJSON.g:135:23: k= json_string ':' v= json_value
                pass 
                self._state.following.append(self.FOLLOW_json_string_in_pair1445)
                k = self.json_string()

                self._state.following.pop()
                self.match(self.input, 36, self.FOLLOW_36_in_pair1447)
                self._state.following.append(self.FOLLOW_json_value_in_pair1451)
                v = self.json_value()

                self._state.following.pop()
                #action start
                out=(k,v)
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return out

    # $ANTLR end "pair"


    # $ANTLR start "json_array"
    # OrderlyJSON.g:137:1: json_array returns [result] : '[' (elem= elements )? ']' ;
    def json_array(self, ):

        result = None

        elem = None


        try:
            try:
                # OrderlyJSON.g:137:29: ( '[' (elem= elements )? ']' )
                # OrderlyJSON.g:137:31: '[' (elem= elements )? ']'
                pass 
                self.match(self.input, 26, self.FOLLOW_26_in_json_array1465)
                # OrderlyJSON.g:137:39: (elem= elements )?
                alt36 = 2
                LA36_0 = self.input.LA(1)

                if (LA36_0 == INTEGER or LA36_0 == STRING or LA36_0 == 21 or LA36_0 == 24 or LA36_0 == 26 or (37 <= LA36_0 <= 38)) :
                    alt36 = 1
                if alt36 == 1:
                    # OrderlyJSON.g:137:39: elem= elements
                    pass 
                    self._state.following.append(self.FOLLOW_elements_in_json_array1469)
                    elem = self.elements()

                    self._state.following.pop()



                self.match(self.input, 27, self.FOLLOW_27_in_json_array1472)
                #action start
                result = elem
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "json_array"


    # $ANTLR start "json_number"
    # OrderlyJSON.g:139:1: json_number returns [result] : i= INTEGER (f= FRAC )? (e= EXP )? ;
    def json_number(self, ):

        result = None

        i = None
        f = None
        e = None

        try:
            try:
                # OrderlyJSON.g:140:3: (i= INTEGER (f= FRAC )? (e= EXP )? )
                # OrderlyJSON.g:140:6: i= INTEGER (f= FRAC )? (e= EXP )?
                pass 
                i=self.match(self.input, INTEGER, self.FOLLOW_INTEGER_in_json_number1491)
                # OrderlyJSON.g:140:17: (f= FRAC )?
                alt37 = 2
                LA37_0 = self.input.LA(1)

                if (LA37_0 == FRAC) :
                    alt37 = 1
                if alt37 == 1:
                    # OrderlyJSON.g:140:17: f= FRAC
                    pass 
                    f=self.match(self.input, FRAC, self.FOLLOW_FRAC_in_json_number1495)



                # OrderlyJSON.g:140:25: (e= EXP )?
                alt38 = 2
                LA38_0 = self.input.LA(1)

                if (LA38_0 == EXP) :
                    alt38 = 1
                if alt38 == 1:
                    # OrderlyJSON.g:140:25: e= EXP
                    pass 
                    e=self.match(self.input, EXP, self.FOLLOW_EXP_in_json_number1500)



                #action start
                                               
                exp = 'e' in locals() and e and e.text or ""
                result = 'f' in locals() and f and float(i.text + f.text + exp) or int(i.text + exp)

                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "json_number"


    # $ANTLR start "elements"
    # OrderlyJSON.g:145:1: elements returns [array] : v= json_value ( ',' v2= json_value )* ;
    def elements(self, ):

        array = None

        v = None

        v2 = None


               
        array = []

        try:
            try:
                # OrderlyJSON.g:148:3: (v= json_value ( ',' v2= json_value )* )
                # OrderlyJSON.g:148:5: v= json_value ( ',' v2= json_value )*
                pass 
                self._state.following.append(self.FOLLOW_json_value_in_elements1522)
                v = self.json_value()

                self._state.following.pop()
                # OrderlyJSON.g:148:18: ( ',' v2= json_value )*
                while True: #loop39
                    alt39 = 2
                    LA39_0 = self.input.LA(1)

                    if (LA39_0 == 31) :
                        alt39 = 1


                    if alt39 == 1:
                        # OrderlyJSON.g:149:3: ',' v2= json_value
                        pass 
                        self.match(self.input, 31, self.FOLLOW_31_in_elements1528)
                        self._state.following.append(self.FOLLOW_json_value_in_elements1532)
                        v2 = self.json_value()

                        self._state.following.pop()
                        #action start
                        array.append(v2) 
                        #action end


                    else:
                        break #loop39
                #action start
                array = [v] + array;
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return array

    # $ANTLR end "elements"


    # $ANTLR start "json_value"
    # OrderlyJSON.g:152:1: json_value returns [result] : (val= json_string | val= json_number | val= json_object | val= json_array | 'true' | 'false' | 'null' );
    def json_value(self, ):

        result = None

        val = None


        try:
            try:
                # OrderlyJSON.g:153:3: (val= json_string | val= json_number | val= json_object | val= json_array | 'true' | 'false' | 'null' )
                alt40 = 7
                LA40 = self.input.LA(1)
                if LA40 == STRING:
                    alt40 = 1
                elif LA40 == INTEGER:
                    alt40 = 2
                elif LA40 == 24:
                    alt40 = 3
                elif LA40 == 26:
                    alt40 = 4
                elif LA40 == 37:
                    alt40 = 5
                elif LA40 == 38:
                    alt40 = 6
                elif LA40 == 21:
                    alt40 = 7
                else:
                    nvae = NoViableAltException("", 40, 0, self.input)

                    raise nvae

                if alt40 == 1:
                    # OrderlyJSON.g:153:6: val= json_string
                    pass 
                    self._state.following.append(self.FOLLOW_json_string_in_json_value1556)
                    val = self.json_string()

                    self._state.following.pop()
                    #action start
                    result = val
                    #action end


                elif alt40 == 2:
                    # OrderlyJSON.g:154:6: val= json_number
                    pass 
                    self._state.following.append(self.FOLLOW_json_number_in_json_value1592)
                    val = self.json_number()

                    self._state.following.pop()
                    #action start
                    result = val
                    #action end


                elif alt40 == 3:
                    # OrderlyJSON.g:155:6: val= json_object
                    pass 
                    self._state.following.append(self.FOLLOW_json_object_in_json_value1628)
                    val = self.json_object()

                    self._state.following.pop()
                    #action start
                    result = val
                    #action end


                elif alt40 == 4:
                    # OrderlyJSON.g:156:6: val= json_array
                    pass 
                    self._state.following.append(self.FOLLOW_json_array_in_json_value1664)
                    val = self.json_array()

                    self._state.following.pop()
                    #action start
                    result = val
                    #action end


                elif alt40 == 5:
                    # OrderlyJSON.g:157:6: 'true'
                    pass 
                    self.match(self.input, 37, self.FOLLOW_37_in_json_value1699)
                    #action start
                    result = True
                    #action end


                elif alt40 == 6:
                    # OrderlyJSON.g:158:6: 'false'
                    pass 
                    self.match(self.input, 38, self.FOLLOW_38_in_json_value1742)
                    #action start
                    result = False
                    #action end


                elif alt40 == 7:
                    # OrderlyJSON.g:159:6: 'null'
                    pass 
                    self.match(self.input, 21, self.FOLLOW_21_in_json_value1784)
                    #action start
                    result = None
                    #action end



            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "json_value"


    # $ANTLR start "json_string"
    # OrderlyJSON.g:164:1: json_string returns [result] : c= STRING ;
    def json_string(self, ):

        result = None

        c = None

        try:
            try:
                # OrderlyJSON.g:164:30: (c= STRING )
                # OrderlyJSON.g:164:32: c= STRING
                pass 
                c=self.match(self.input, STRING, self.FOLLOW_STRING_in_json_string1839)
                #action start
                result = str(c.text[1:-1])
                #action end




            except RecognitionException, re:
                self.reportError(re)
                self.recover(self.input, re)
        finally:

            pass
        return result

    # $ANTLR end "json_string"


    # Delegated rules


 

    FOLLOW_unnamed_entries_in_orderly_schema97 = frozenset([1, 17])
    FOLLOW_17_in_orderly_schema100 = frozenset([1])
    FOLLOW_named_entry_in_named_entries123 = frozenset([1, 17])
    FOLLOW_17_in_named_entries131 = frozenset([18, 19, 20, 21, 22, 23, 28, 29, 30])
    FOLLOW_named_entry_in_named_entries135 = frozenset([1, 17])
    FOLLOW_unnamed_entry_in_unnamed_entries164 = frozenset([1, 17])
    FOLLOW_17_in_unnamed_entries173 = frozenset([18, 19, 20, 21, 22, 23, 28, 29, 30])
    FOLLOW_unnamed_entry_in_unnamed_entries177 = frozenset([1, 17])
    FOLLOW_definition_prefix_in_named_entry204 = frozenset([9, 13])
    FOLLOW_property_name_in_named_entry208 = frozenset([8, 26, 32, 33, 35])
    FOLLOW_definition_suffix_in_named_entry212 = frozenset([1])
    FOLLOW_string_prefix_in_named_entry225 = frozenset([9, 13])
    FOLLOW_property_name_in_named_entry229 = frozenset([7, 8, 26, 32, 33, 35])
    FOLLOW_string_suffix_in_named_entry233 = frozenset([1])
    FOLLOW_definition_prefix_in_unnamed_entry264 = frozenset([8, 26, 32, 33, 35])
    FOLLOW_definition_suffix_in_unnamed_entry268 = frozenset([1])
    FOLLOW_string_prefix_in_unnamed_entry280 = frozenset([7, 8, 26, 32, 33, 35])
    FOLLOW_string_suffix_in_unnamed_entry284 = frozenset([1])
    FOLLOW_18_in_definition_prefix313 = frozenset([1, 24])
    FOLLOW_optional_range_in_definition_prefix317 = frozenset([1])
    FOLLOW_19_in_definition_prefix386 = frozenset([1, 24])
    FOLLOW_optional_range_in_definition_prefix390 = frozenset([1])
    FOLLOW_20_in_definition_prefix460 = frozenset([1])
    FOLLOW_21_in_definition_prefix548 = frozenset([1])
    FOLLOW_22_in_definition_prefix639 = frozenset([1])
    FOLLOW_23_in_definition_prefix731 = frozenset([24, 26])
    FOLLOW_24_in_definition_prefix742 = frozenset([17, 18, 19, 20, 21, 22, 23, 25, 28, 29, 30])
    FOLLOW_unnamed_entries_in_definition_prefix746 = frozenset([17, 25])
    FOLLOW_17_in_definition_prefix749 = frozenset([25])
    FOLLOW_25_in_definition_prefix752 = frozenset([1, 6, 24])
    FOLLOW_OPTIONAL_ADDITIONAL_MARKER_in_definition_prefix756 = frozenset([1, 24])
    FOLLOW_optional_range_in_definition_prefix761 = frozenset([1])
    FOLLOW_26_in_definition_prefix778 = frozenset([17, 18, 19, 20, 21, 22, 23, 27, 28, 29, 30])
    FOLLOW_unnamed_entry_in_definition_prefix782 = frozenset([17, 27])
    FOLLOW_17_in_definition_prefix785 = frozenset([27])
    FOLLOW_27_in_definition_prefix788 = frozenset([1, 24])
    FOLLOW_optional_range_in_definition_prefix792 = frozenset([1])
    FOLLOW_28_in_definition_prefix844 = frozenset([24])
    FOLLOW_24_in_definition_prefix846 = frozenset([17, 18, 19, 20, 21, 22, 23, 25, 28, 29, 30])
    FOLLOW_named_entries_in_definition_prefix850 = frozenset([17, 25])
    FOLLOW_17_in_definition_prefix853 = frozenset([25])
    FOLLOW_25_in_definition_prefix856 = frozenset([1, 6])
    FOLLOW_OPTIONAL_ADDITIONAL_MARKER_in_definition_prefix860 = frozenset([1])
    FOLLOW_29_in_definition_prefix890 = frozenset([24])
    FOLLOW_24_in_definition_prefix893 = frozenset([17, 18, 19, 20, 21, 22, 23, 25, 28, 29, 30])
    FOLLOW_unnamed_entries_in_definition_prefix897 = frozenset([17, 25])
    FOLLOW_17_in_definition_prefix900 = frozenset([25])
    FOLLOW_25_in_definition_prefix903 = frozenset([1])
    FOLLOW_30_in_string_prefix969 = frozenset([1, 24])
    FOLLOW_optional_range_in_string_prefix973 = frozenset([1])
    FOLLOW_OPTIONAL_PERL_REGEX_in_string_suffix991 = frozenset([8, 26, 32, 33, 35])
    FOLLOW_definition_suffix_in_string_suffix996 = frozenset([1])
    FOLLOW_optional_enum_values_in_definition_suffix1012 = frozenset([1, 8, 32, 33, 35])
    FOLLOW_optional_default_value_in_definition_suffix1018 = frozenset([1, 8, 32, 33])
    FOLLOW_optional_requires_in_definition_suffix1024 = frozenset([1, 8, 32])
    FOLLOW_OPTIONAL_OPTIONAL_MARKER_in_definition_suffix1030 = frozenset([1, 32])
    FOLLOW_optional_extra_properties_in_definition_suffix1036 = frozenset([1])
    FOLLOW_property_name_in_csv_property_names1062 = frozenset([1, 31])
    FOLLOW_31_in_csv_property_names1072 = frozenset([9, 13])
    FOLLOW_property_name_in_csv_property_names1076 = frozenset([1, 31])
    FOLLOW_32_in_optional_extra_properties1113 = frozenset([24])
    FOLLOW_json_object_in_optional_extra_properties1117 = frozenset([32])
    FOLLOW_32_in_optional_extra_properties1119 = frozenset([1])
    FOLLOW_33_in_optional_requires1137 = frozenset([9, 13])
    FOLLOW_csv_property_names_in_optional_requires1141 = frozenset([34])
    FOLLOW_34_in_optional_requires1143 = frozenset([1])
    FOLLOW_json_array_in_optional_enum_values1178 = frozenset([1])
    FOLLOW_35_in_optional_default_value1193 = frozenset([10, 13, 21, 24, 26, 37, 38])
    FOLLOW_json_value_in_optional_default_value1197 = frozenset([1])
    FOLLOW_24_in_optional_range1212 = frozenset([10, 31])
    FOLLOW_json_number_in_optional_range1216 = frozenset([31])
    FOLLOW_31_in_optional_range1219 = frozenset([10, 25])
    FOLLOW_json_number_in_optional_range1223 = frozenset([25])
    FOLLOW_25_in_optional_range1226 = frozenset([1])
    FOLLOW_json_string_in_property_name1244 = frozenset([1])
    FOLLOW_PROPERTY_NAME_TOKEN_in_property_name1282 = frozenset([1])
    FOLLOW_24_in_json_object1380 = frozenset([13, 25])
    FOLLOW_members_in_json_object1384 = frozenset([25])
    FOLLOW_25_in_json_object1387 = frozenset([1])
    FOLLOW_pair_in_members1410 = frozenset([1, 31])
    FOLLOW_31_in_members1416 = frozenset([13])
    FOLLOW_pair_in_members1420 = frozenset([1, 31])
    FOLLOW_json_string_in_pair1445 = frozenset([36])
    FOLLOW_36_in_pair1447 = frozenset([10, 13, 21, 24, 26, 37, 38])
    FOLLOW_json_value_in_pair1451 = frozenset([1])
    FOLLOW_26_in_json_array1465 = frozenset([10, 13, 21, 24, 26, 27, 37, 38])
    FOLLOW_elements_in_json_array1469 = frozenset([27])
    FOLLOW_27_in_json_array1472 = frozenset([1])
    FOLLOW_INTEGER_in_json_number1491 = frozenset([1, 11, 12])
    FOLLOW_FRAC_in_json_number1495 = frozenset([1, 12])
    FOLLOW_EXP_in_json_number1500 = frozenset([1])
    FOLLOW_json_value_in_elements1522 = frozenset([1, 31])
    FOLLOW_31_in_elements1528 = frozenset([10, 13, 21, 24, 26, 37, 38])
    FOLLOW_json_value_in_elements1532 = frozenset([1, 31])
    FOLLOW_json_string_in_json_value1556 = frozenset([1])
    FOLLOW_json_number_in_json_value1592 = frozenset([1])
    FOLLOW_json_object_in_json_value1628 = frozenset([1])
    FOLLOW_json_array_in_json_value1664 = frozenset([1])
    FOLLOW_37_in_json_value1699 = frozenset([1])
    FOLLOW_38_in_json_value1742 = frozenset([1])
    FOLLOW_21_in_json_value1784 = frozenset([1])
    FOLLOW_STRING_in_json_string1839 = frozenset([1])



       
def main(argv, otherArg=None):
  char_stream = ANTLRFileStream(sys.argv[1])
  lexer = OrderlyJSONLexer(char_stream)

  tokens = CommonTokenStream(lexer)
  parser = OrderlyJSONParser(tokens);

  try:
        print parser.orderly_schema()
  except RecognitionException:
	traceback.print_stack()


if __name__ == '__main__':
    main(sys.argv)
