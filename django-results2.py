[INPUT]
if match :
[GROUND TRUTH]
# host ends with ' . ' and host ends with pattern or host is equal to all but first elements of pattern ,   substitute boolean true for match , otherwise substitute boolean False for match .   if match is true ,
[PREDICTED]
# if if is true ,

[INPUT]
self . stdout . write ( ' \n ' . join ( sorted ( registry . tags_available ( ) ) ) )
[GROUND TRUTH]
# call the method registry . tags_available , sort the result and join it into a string , separate by newlines , write it to self . stdout .
[PREDICTED]
# call the method self . write with an argument \n , use the result as an argument for the call to the method self . stdout .

[INPUT]
for ( k , v ) in type _ . _ _ dict _ _ . items ( ) :
[GROUND TRUTH]
# for every k and v in result of the call to the method type _ . _ _ dict _ _ . items ,
[PREDICTED]
# for every k and v in return value of the method _ _ . _ _ _ _ _ _ _ _ . _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

[INPUT]
def iteritems ( d , * * kw ) :
[GROUND TRUTH]
# return it .   define the function iteritems with 2 arguments : d and unpacked dictionary kw .
[PREDICTED]
# define the function iteritems with 2 arguments : unpacked list args and unpacked dictionary kwargs .

[INPUT]
lookup_view = get_callable ( lookup_view , True )
[GROUND TRUTH]
# call the function get_callable with arguments lookup_view and boolean True , substitute the result for lookup_view .
[PREDICTED]
# call the function get_callable with arguments lookup_view and integer 0 , substitute the result for lookup_view .

[INPUT]
with open ( filepath , ' rb ' ) as fp :
[GROUND TRUTH]
# open the file named filepath in read mode , with file descriptor renamed to fp perform ,
[PREDICTED]
# with 2 arguments : filepath and string ' rb ' , write it to self . stdout .   call the function open with 2 arguments : string ' rb ' and fp ,

[INPUT]
return formataddr ( ( nm , addr ) )
[GROUND TRUTH]
# call the formataddr function with argument tuple containing 2 elements nm and addr .
[PREDICTED]
# call the function formataddr with 2 arguments : return value of the function ( , return the result .

[INPUT]
def render_node ( self , node , context ) :
[GROUND TRUTH]
# define the method render_node with 3 arguments : self , node and context .
[PREDICTED]
# define the method render_node with 3 arguments : self , node and context .

[INPUT]
return strip_tags ( value )
[GROUND TRUTH]
# call the function strip_tags with an argument value , return the result .
[PREDICTED]
# call the function strip_tags with an argument value , return the result .

[INPUT]
def walk_to_end ( ch , input_iter ) :
[GROUND TRUTH]
# define the function walk_to_end with 2 arguments ch and input_iter .
[PREDICTED]
# define the function walk_to_end with 2 arguments : ch and input_iter .

[INPUT]
best_doublecolon_end = ( best_doublecolon_start + best_doublecolon_len )
[GROUND TRUTH]
# sum best_doublecolon_start and best_doublecolon_len , substitute the result for best_doublecolon_end ,
[PREDICTED]
# sum best_doublecolon_start and best_doublecolon_len , substitute the result for best_doublecolon_end ,

[INPUT]
_ assertRegex = " assertRegexpMatches "
[GROUND TRUTH]
# _ assertRegex is a strnig " assertRegexpMatches " .
[PREDICTED]
# _ _ " is a strnig " " " .

[INPUT]
def open ( self ) :
[GROUND TRUTH]
# define the method open with argument self .
[PREDICTED]
# define the method open with argument self .

[INPUT]
def tags_available ( self ) :
[GROUND TRUTH]
# define the method tags_available with argument self .
[PREDICTED]
# define the method tags_available with an argument self .

[INPUT]
repr_attr = self . _ setupfunc
[GROUND TRUTH]
# substitute self . _ setupfunc for repr_attr .
[PREDICTED]
# substitute self . _ _ for repr_attr .

[INPUT]
self . deprecation_warning = deprecation_warning
[GROUND TRUTH]
# substitute deprecation_warning for self . deprecation_warning .
[PREDICTED]
# substitute deprecation_warning for self . deprecation_warning .

[INPUT]
except Exception :
[GROUND TRUTH]
# if Exception exception is caught ,
[PREDICTED]
# if Exception exception is caught ,

[INPUT]
return template
[GROUND TRUTH]
# return template .
[PREDICTED]
# return template .

[INPUT]
try :
[GROUND TRUTH]
# try ,
[PREDICTED]
# try ,

[INPUT]
try :
[GROUND TRUTH]
# try ,
[PREDICTED]
# try ,

[INPUT]
boundarystream = InterBoundaryIter ( self . _ stream , self . _ separator )
[GROUND TRUTH]
# boundarystream is an instance of InterBoundaryIter class , created with self . _ stream and self . _ separator as arguments .
[PREDICTED]
# get the attribute ' self ' key of the self . _ _ _ _ _ _ , substitute it for self .

[INPUT]
db_name = connection . creation . create_test_db ( verbosity = verbosity , autoclobber = not interactive , serialize = False )
[GROUND TRUTH]
# call the method connection . creation . create_test_db with verbosity set to verbosity , autoclobber set to inverse value of interactive ,
[PREDICTED]
# call the method connection . creation . creation . creation . creation . creation . creation . create_test_db with verbosity set to verbosity

[INPUT]
self . upload_handlers = ImmutableList ( self . upload_handlers , warning = " You can not alter upload handlers after the upload has been processed . " )
[GROUND TRUTH]
# self . upload_handlers is an instance of ImmutableList , created with 2 arguments : self . upload_handlers ,
[PREDICTED]
# self . upload_handlers is an instance of a class self . upload_handlers , called with an argument self . upload_handlers ,

[INPUT]
if iso_input not in val :
[GROUND TRUTH]
# for every iso_input in the result ,   if iso_input is not contained in val ,
[PREDICTED]
# if if if is not contained in val ,

[INPUT]
token = get_token ( request )
[GROUND TRUTH]
# call the function get_token with an argument request , substitute the result for token .
[PREDICTED]
# call the function get_token with an argument request , substitute the result for token .

[INPUT]
from django . db . migrations . loader import AmbiguityError
[GROUND TRUTH]
# from django . db . migrations . loader import AmbiguityError into default name space .
[PREDICTED]
# from django . migrations . migrations . loader import import into default name space .

[INPUT]
self . current_token = self . next_token ( )
[GROUND TRUTH]
# call the method self . next_token , substitute the result for self . current_token .
[PREDICTED]
# call the method self . . substitute with an argument self .

[INPUT]
@ register . filter ( is_safe = False )
[GROUND TRUTH]
# decorator function register . filter with an argument is_safe set to boolean False .
[PREDICTED]
# decorator function register . filter with an argument is_safe set to boolean False .

[INPUT]
from django . utils . translation import get_language
[GROUND TRUTH]
# from django . utils . translation import get_language into default name space .
[PREDICTED]
# from django . utils . translation import import into default name space .

[INPUT]
from django . utils . encoding import python_2_unicode_compatible
[GROUND TRUTH]
# from django . utils . encoding import python_2_unicode_compatible into default name space .
[PREDICTED]
# from django . utils . encoding import import into default name space .

[INPUT]
return self . _ _ offset ,
[GROUND TRUTH]
# return a tuple with an element self . _ _ offset .
[PREDICTED]
# return self . _ _ _ _ _ _ _ .

[INPUT]
return self . as_table ( )
[GROUND TRUTH]
# call the method self . as_table , return the result .
[PREDICTED]
# call the method self . . , return the result .

[INPUT]
from django . conf import settings
[GROUND TRUTH]
# from django . conf import settings into default namespace .
[PREDICTED]
# from django . conf import settings into default name space .

[INPUT]
self . _ cached_loaders = [ ]
[GROUND TRUTH]
# self . _ cached_loaders is an empty list .
[PREDICTED]
# self . _ _ is an empty list .

[INPUT]
self . bcc = [ ]
[GROUND TRUTH]
# self . bcc is an empty list .
[PREDICTED]
# self . . is an empty list .

[INPUT]
return ' 0 '
[GROUND TRUTH]
# return an string ' 0 ' .
[PREDICTED]
# return string ' 0 ' .

[INPUT]
if error . params :
[GROUND TRUTH]
# if error . params is true ,
[PREDICTED]
# if if . . is true ,

[INPUT]
return True
[GROUND TRUTH]
# return boolean True .
[PREDICTED]
# return boolean True .

[INPUT]
else :
[GROUND TRUTH]
# if not ,
[PREDICTED]
# if not ,

[INPUT]
import imp
[GROUND TRUTH]
# import imp .
[PREDICTED]
# import module import .

[INPUT]
options = [ opt for opt in options if opt [ 0 ] not in prev_opts ]
[GROUND TRUTH]
# split x by character ' = ' and append first element of the result to the prev_opts list .   for every opt in options , if first element of opt is not contained in prev_opts , append opt to the list , substitute it for options .
[PREDICTED]
# for every opt in opt , append the result to a list , append to the resulting list list with an element : opt , for every opt in opt ,

[INPUT]
ADDRESS_HEADERS = set ( [ ' from ' , ' sender ' , ' reply - to ' , ' to ' , ' cc ' , ' bcc ' , ' resent - from ' , ' resent - sender ' , ' resent - to ' , ' resent - cc ' , ' resent - bcc ' , ] )
[GROUND TRUTH]
# ADDRESS_HEADERS is a set containing strings : ' from ' , ' sender ' , ' reply - to ' , ' to ' , ' cc ' , ' bcc ' , ' resent - from ' , ' resent - sender ' ,
[PREDICTED]
# ' ' ' , ' resent ' for ' , ' , ' for ' , ' for ' , ' for ' , ' for ' , ' for ' , ' for ' , ' for ' , ' for ' ' ' ' , ' x

[INPUT]
else :
[GROUND TRUTH]
# return value of the function quote called with arguments k and safe , and with return value of the function quote called with arguments v and safe .   if not ,
[PREDICTED]
# if not ,

[INPUT]
@ property
[GROUND TRUTH]
# where ' % s ' is replaced with self . _ _ class _ _ . _ _ name _ _ .   property decorator ,
[PREDICTED]
# property decorator ,

[INPUT]
raise InvalidTemplateLibrary ( " Unsupported arguments to " " Library . filter : ( % r , % r ) " , ( name , filter_func ) )
[GROUND TRUTH]
# raise an InvalidTemplateLibrary exception with an argument string ( " Unsupported arguments to Library . filter : ( % r , % r ) " ,
[PREDICTED]
# raise an InvalidTemplateLibrary exception with an argument string " Unsupported arguments % s . " , where ' % s ' is replaced by :

[INPUT]
IDENTIFIER = re . compile ( ' ^[a - z_][a - z0 - 9_]*$ ' , re . I )
[GROUND TRUTH]
# compile regex from string ' ^[a - z_][a - z0 - 9_]*$ ' in case insensitive mode , substitute it for IDENTIFIER .
[PREDICTED]
# call the function re . compile with 2 arguments : raw string ' < - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

[INPUT]
if len ( fixture_files_in_dir ) > 1 :
[GROUND TRUTH]
# and result of the function humanize called with an argument fixture_dir .   if length of fixture_files_in_dir is greater than 1 ,
[PREDICTED]
# if length of fixture_files_in_dir is not equal to integer 1 ,

[INPUT]
raise NotImplementedError ( ' subclasses of Storage must provide a url ( ) method ' )
[GROUND TRUTH]
# raise an NotImplementedError exception with argument string ' subclasses of Storage must provide a url ( ) method ' .
[PREDICTED]
# raise an NotImplementedError exception with argument string ' subclasses of ' subclasses of provide ( ) ( ) ' .

[INPUT]
max_value = self . max_expr . resolve ( context )
[GROUND TRUTH]
# call the method self . max_expr . resolve with an argument context , substitute the result for max_value .
[PREDICTED]
# call the method self . resolve with an argument context , substitute the result for max_value .

[INPUT]
def value_from_datadict ( self , data , files , name ) :
[GROUND TRUTH]
# define the method value_from_datadict with 4 arguments : self , data , files and name .
[PREDICTED]
# define the method value_from_datadict with 3 arguments : self , data , data and name set to boolean False .

[INPUT]
from django . core . serializers . base import SerializerDoesNotExist
[GROUND TRUTH]
# from django . core . serializers . base import SerializerDoesNotExist into default name space .
[PREDICTED]
# from django . base . base . base import import into default name space .

[INPUT]
def _ has_changed ( self , initial , data ) :
[GROUND TRUTH]
# define the method _ has_changed with 3 arguments : self , initial and data .
[PREDICTED]
# define the method _ _ has_changed with arguments self , initial and data .

[INPUT]
link [ NEXT ] = root
[GROUND TRUTH]
# substitute root for value under the NEXT key of the link dictionary .
[PREDICTED]
# substitute link for value under the link key of the link dictionary .

[INPUT]
d = Decimal ( input_val )
[GROUND TRUTH]
# d is an instance of Decimal class created with an argument input_val .
[PREDICTED]
# call the function Decimal with an argument input_val , substitute the result for d .

[INPUT]
from django . conf import settings
[GROUND TRUTH]
# from django . conf import settings into default name space .
[PREDICTED]
# from django . conf import settings into default name space .

[INPUT]
time . sleep ( 1 )
[GROUND TRUTH]
# call the function time . sleep with argument integer 1 .
[PREDICTED]
# call the function time . sleep with an argument integer 1 .

[INPUT]
data = str ( data )
[GROUND TRUTH]
# convert data to string , substitute it for data .
[PREDICTED]
# convert data into a string , substitute it for data .

[INPUT]
def rendered_content ( self ) :
[GROUND TRUTH]
# define the method rendered_content with an argument self .
[PREDICTED]
# define the method rendered_content with an argument self .

[INPUT]
if six . PY3 :
[GROUND TRUTH]
# if six . PY3 is true ,
[PREDICTED]
# if if . . . is true ,

[INPUT]
else :
[GROUND TRUTH]
# if not ,
[PREDICTED]
# if not ,

[INPUT]
if self . META . get ( ' CONTENT_TYPE ' , '' ) . startswith ( ' multipart / form - data ' ) :
[GROUND TRUTH]
# get the value under the ' CONTENT_TYPE ' key of the self . META dictionary , if it starts with a string ' multipart / form - data ' ,
[PREDICTED]
# if self . get has an attribute ' CONTENT_TYPE ' ,

[INPUT]
raise PageNotAnInteger ( ' That page number is not an integer ' )
[GROUND TRUTH]
# raise an exception PageNotAnInteger with string ' That page number is not an integer ' as an argument .
[PREDICTED]
# raise an PageNotAnInteger exception with an argument string ' That number number not not not not not not an not ' .

[INPUT]
size = property ( _ get_size , _ set_size )
[GROUND TRUTH]
# size is a property object with _ get_size as getter method and _ set_size as setter method .
[PREDICTED]
# get the attribute named _ _ _ _ _ _ _ _ , substitute it for _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

[INPUT]
return I18N_MODIFIED if filename . endswith ( ' . mo ' ) else FILE_MODIFIED
[GROUND TRUTH]
# if filename ends with string ' . mo ' return I18N_MODIFIED , otherwise return FILE_MODIFIED .
[PREDICTED]
# if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if if

[INPUT]
def _ _ repr _ _ ( self ) :
[GROUND TRUTH]
# define the method _ _ repr _ _ with an argument self .
[PREDICTED]
# define the method _ _ repr _ _ with an argument self .

[INPUT]
class SerializationError ( Exception ) :
[GROUND TRUTH]
# derive the class SerializationError from the Exception base class .
[PREDICTED]
# derive the class class from the Exception base class .

[INPUT]
def has_other_pages ( self ) :
[GROUND TRUTH]
# define the method has_other_pages with an argument self .
[PREDICTED]
# define the method has_other_pages with an argument self .

[INPUT]
def escape_quotes ( m ) :
[GROUND TRUTH]
# define the function escape_quotes with an argument m .
[PREDICTED]
# define the function escape_quotes with an argument m .

[INPUT]
def next_token ( self ) :
[GROUND TRUTH]
# define the method next_token with an argument self .
[PREDICTED]
# define the method next_token with an argument self .

[INPUT]
if upto ! = start :
[GROUND TRUTH]
# if upto is not equal to start .
[PREDICTED]
# if if is not None ,

[INPUT]
self . waiting_readers = 0
[GROUND TRUTH]
# self . waiting_readers is an integer 0 .
[PREDICTED]
# self . . is an integer 0 .

[INPUT]
except ImportError :
[GROUND TRUTH]
# if ImportError exception is caught ,
[PREDICTED]
# if ImportError exception is caught ,

[INPUT]
for location in format_locations :
[GROUND TRUTH]
# for every location in format_locations ,
[PREDICTED]
# for every location in format_locations ,

[INPUT]
supports_microseconds = False
[GROUND TRUTH]
# supports_microseconds is boolean False .
[PREDICTED]
# supports_microseconds is boolean False .

[INPUT]
return " "
[GROUND TRUTH]
# return an empty string .
[PREDICTED]
# return an empty string .

[INPUT]
import cgi
[GROUND TRUTH]
# import module cgi .
[PREDICTED]
# import module import module .

[INPUT]
else :
[GROUND TRUTH]
# if not ,
[PREDICTED]
# if not ,

[INPUT]
@ property
[GROUND TRUTH]
# property decorator .
[PREDICTED]
# property decorator ,

[INPUT]
@ property
[GROUND TRUTH]
# property decorator ,
[PREDICTED]
# property decorator ,

[INPUT]
else :
[GROUND TRUTH]
# if not ,
[PREDICTED]
# if not ,

[INPUT]
else :
[GROUND TRUTH]
# " Django 1 . 7 changed the global defaults for the MIDDLEWARE_CLASSES . django . contrib . sessions . middleware . SessionMiddleware ,   django . contrib . auth . middleware . AuthenticationMiddleware , and django . contrib . messages . middleware . MessageMiddleware were removed   from the defaults . If your project needs these middleware then you should configure this setting . " , obj set to None , and   i d set to a string ' 1_7 . W001 ' , put the result into a list and return it .   if not ,
[PREDICTED]
# if not ,

[INPUT]
def set ( self , key , value , timeout = DEFAULT_TIMEOUT , version = None ) :
[GROUND TRUTH]
# define the method set with 5 arguments , self class instance , key , value , timeout set to DEFAULT_TIMEOUT and version set to None .
[PREDICTED]
# define the method set with 5 arguments , self class instance , value , value , value , value and version set to None .

[INPUT]
context_extras [ ' LANGUAGE_BIDI ' ] = translation . get_language_bidi ( )
[GROUND TRUTH]
# call the translation . get_language_bidi function , substitute the result for the value under the ' LANGUAGE_BIDI ' key of the context_extras dictionary .
[PREDICTED]
# call the method translation . get_language_bidi , substitute the result for value under the ' LANGUAGE_BIDI ' key of the context_extras dictionary .

[INPUT]
errors = [ model . check ( * * kwargs ) for model in apps . get_models ( ) if app_configs is None or model . _ meta . app_config in app_configs ]
[GROUND TRUTH]
# call the model . check method with unpacked dictionary kwargs for every model in return value of function apps . get_models ,
[PREDICTED]
# for every app_configs in return value of the function model . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta . _ meta

[INPUT]
statements = sql_custom ( app_config , self . style , connection )
[GROUND TRUTH]
# call the function sql_custom with app_config , self . style and connection as the arguments , substitute the result for statements .
[PREDICTED]
# call the function sql_custom with 2 arguments : self . style and self . style , substitute the result for statements .

[INPUT]
for model in router . get_migratable_models ( app_config , connection . alias , include_auto_created = True ) :
[GROUND TRUTH]
# for model in router . get_migratable_models method return value , called with 3 arguments : app_config , connection . alias ,
[PREDICTED]
# for every model in return value of the method connection . get_migratable_models with arguments ,

[INPUT]
factory = klass
[GROUND TRUTH]
# substitute the result for value under ' address ' key of config dictionary .   substitute klass for factory .
[PREDICTED]
# substitute it for value under the ' _ ' key of the self . _ dictionary .   substitute klass for factory .

[INPUT]
if self . data . minute = = 0 and self . data . hour = = 12 :
[GROUND TRUTH]
# if self . data . minute equals integer 0 and self . data . hour equals integer 12 ,
[PREDICTED]
# if self . data . data equals integer 0 and self . data . data equals integer 0 ,

[INPUT]
as_form = True
[GROUND TRUTH]
# where ' % s ' is replaced with last element of args .   as_form is boolean True
[PREDICTED]
# as_form is boolean True .

[INPUT]
from django . db . models . fields . related import RelatedObject
[GROUND TRUTH]
# from django . db . models . fields . related import RelatedObject into default namespace .
[PREDICTED]
# from django . db . models . related import import into default name space .

[INPUT]
parser . add_argument ( ' --pythonpath ' )
[GROUND TRUTH]
# call the method parser . add_argument with an argument string ' --pythonpath ' .
[PREDICTED]
# call the method parser . add_argument with an argument string ' --pythonpath ' .

[INPUT]
def _ _ str _ _ ( self ) :
[GROUND TRUTH]
# define the method _ _ str _ _ with an argument self .
[PREDICTED]
# define the method _ _ str _ _ with an argument self .

[INPUT]
return '' . join ( base36 )
[GROUND TRUTH]
# join elements of base36 into a string , return it .
[PREDICTED]
# join elements of '' into a string , return it .

[INPUT]
httpd . daemon_threads = True
[GROUND TRUTH]
# httpd . daemon_threads is boolean True .
[PREDICTED]
# httpd . . is boolean True .

[INPUT]
self . func = func
[GROUND TRUTH]
# substitute func for self . func .
[PREDICTED]
# substitute func for self . func .

[INPUT]
except AmbiguityError :
[GROUND TRUTH]
# if AmbiguityError exception is caught ,
[PREDICTED]
# if AmbiguityError exception is caught ,

[INPUT]
WindowsError = WindowsError
[GROUND TRUTH]
# substitute WindowsError for WindowsError .
[PREDICTED]
# substitute WindowsError for WindowsError .

[INPUT]
else :
[GROUND TRUTH]
# if not ,
[PREDICTED]
# if not ,

[INPUT]
pass
[GROUND TRUTH]
# do nothing .
[PREDICTED]
# do nothing .

[INPUT]
try :
[GROUND TRUTH]
# try ,
[PREDICTED]
# try ,

[INPUT]
stderr . write ( ' % s : % s ' % ( e . _ _ class _ _ . _ _ name _ _ , e ) )
[GROUND TRUTH]
# created with arguments sys . stderr and self . style . ERROR .   replace ' % s ' in string ' % s : % s ' with e . _ _ class _ _ . _ _ name _ _ and e , respectively , write it to the stderr stream .
[PREDICTED]
# call the method _ _ init _ _ from the base class of the class _ , with 2 arguments : string ' % s ' formated with e .

[INPUT]
_ _ all _ _ = ( ' Field ' , ' CharField ' , ' IntegerField ' , ' DateField ' , ' TimeField ' , ' DateTimeField ' , ' RegexField ' , ' EmailField ' , ' FileField ' , ' ImageField ' , ' URLField ' , ' BooleanField ' , ' NullBooleanField ' , ' ChoiceField ' , ' MultipleChoiceField ' , ' ComboField ' , ' MultiValueField ' , ' FloatField ' , ' DecimalField ' , ' SplitDateTimeField ' , ' IPAddressField ' , ' GenericIPAddressField ' , ' FilePathField ' , ' SlugField ' , ' TypedChoiceField ' , ' TypedMultipleChoiceField ' )
[GROUND TRUTH]
# _ _ all _ _ a tuple containing strings : ' Field ' , ' CharField ' , ' IntegerField ' , ' DateField ' , ' TimeField ' , ' DateTimeField ' , ' RegexField ' ,
[PREDICTED]
# ' ' , ' for ' , ' , ' for ' , ' for ' , ' for ' , ' for ' , ' for ' , ' for ' , ' for ' , ' for ' , ' for ' , ' for ' , ' for ' ' ' '

[INPUT]
DEFAULT_PALETTE = DARK_PALETTE
[GROUND TRUTH]
# a dictionary with 18 pairs of dictionary value and string keys for DARK_PALETTE ,   and a dictionary with 18 pairs of dictionary value and string keys for LIGHT_PALETTE .   substitute DARK_PALETTE for DEFAULT_PALETTE .
[PREDICTED]
# where ' % s ' is replaced with name and app_label , respectively .   if not ,

[INPUT]
answer = six . moves . input ( " Do you wish to proceed ? [ yN ] " )
[GROUND TRUTH]
# call the method six . moves . input with an argument string " Do you wish to proceed ? [ yN ] " , substitute the result for answer .
[PREDICTED]
# call the method six . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves . moves .

[INPUT]
raise NotImplementedError ( ' subclasses of BaseCache must provide a delete ( ) method ' )
[GROUND TRUTH]
# raise an exception of class NotImplementedError , with string ' subclasses of BaseCache must provide a delete ( ) method ' as argument .
[PREDICTED]
# raise an NotImplementedError exception with argument string ' subclasses of ' subclasses of ' ' ' for '

[INPUT]
localpart = str ( Header ( localpart , encoding ) )
[GROUND TRUTH]
# instantiate Header class with localpart and encoding , convert it to a string , substitute the result for localpart .
[PREDICTED]
# call the function str with 2 arguments : localpart and encoding , substitute the result for localpart and encoding , respectively .

[INPUT]
e , tb = sys . exc_info ( ) [ 1 : ]
[GROUND TRUTH]
# call the method sys . exc_info , substitute the result without the first element for e and tb .
[PREDICTED]
# call the method sys . exc_info , substitute the result without the first element for e .

[INPUT]
endpos = self . check_for_whole_start_tag ( i )
[GROUND TRUTH]
# call the method self . check_for_whole_start_tag with i as an argument , substitute result for the endpos .
[PREDICTED]
# call the method self . check_for_whole_start_tag with an argument i , substitute the result for endpos .

[INPUT]
re_escaped = re . compile ( r'\\ ( . ) ' )
[GROUND TRUTH]
# compile regex from a string ' \\ ( . ) ' , substitute it for re_escaped .
[PREDICTED]
# call the function re . ) with an argument string ' ( ) ' , substitute the result for re_escaped .

[INPUT]
def check_all_models ( app_configs = None , * * kwargs ) :
[GROUND TRUTH]
# define the function check_all_models with app_configs defaulting to None and unpacked dictionary kwargs as arguments .
[PREDICTED]
# define the function check_all_models with 2 arguments : unpacked list args and unpacked dictionary kwargs .

[INPUT]
form . data [ form . add_prefix ( self . _ pk_field . name ) ] = None
[GROUND TRUTH]
# call the method form . add_prefix with an argument self . _ pk_field . name ,
[PREDICTED]
# call the method form . _ _ . _ _ with an argument self . _ _ class _ _ , use the result as an argument for the call to the function form . _ _ . _ _ name _ _ .

[INPUT]
def _ _ setstate _ _ ( self , state ) :
[GROUND TRUTH]
# define the method _ _ setstate _ _ with 2 arguments : self and state .
[PREDICTED]
# define the method _ _ init _ _ with 2 arguments self and state .

[INPUT]
from django . core . files . move import file_move_safe
[GROUND TRUTH]
# from django . core . files . move import file_move_safe into default name space .
[PREDICTED]
# from django . files . files . move import import into default name space .

[INPUT]
query_string = query_string . decode ( )
[GROUND TRUTH]
# call the method query_string . decode , substitute the result for query_string .
[PREDICTED]
# call the method query_string . . .

[INPUT]
def size ( self , name ) :
[GROUND TRUTH]
# define the method size with arguments self and name .
[PREDICTED]
# define the method size with 2 arguments self and name .

[INPUT]
def d ( self ) :
[GROUND TRUTH]
# define the method d with an argument self .
[PREDICTED]
# define the method d with an argument self .

[INPUT]
def _ list_cache_files ( self ) :
[GROUND TRUTH]
# define the method _ list_cache_files with argument self .
[PREDICTED]
# define the method _ _ list_cache_files with an argument self .

[INPUT]
template_dirs = settings . TEMPLATE_DIRS
[GROUND TRUTH]
# substitute settings . TEMPLATE_DIRS for template_dirs .
[PREDICTED]
# substitute settings . template_dirs for template_dirs .

[INPUT]
new_second_item . extend ( item )
[GROUND TRUTH]
# extend new_second_item with item .
[PREDICTED]
# call the method extend with an argument item .

[INPUT]
yield v
[GROUND TRUTH]
# yield v .
[PREDICTED]
# yield one element of the result .

[INPUT]
def _ _ init _ _ ( self , _ subtype = ' mixed ' , boundary = None , _ subparts = None , encoding = None , * * _ params ) :
[GROUND TRUTH]
# define the method _ _ init _ _ with 6 arguments : self , _ subtype set to string ' mixed ' , boundary set to None , _ subparts set to None ,
[PREDICTED]
# define the method _ _ init _ _ with 3 arguments : self , unpacked list args and unpacked dictionary kwargs .

[INPUT]
data_value = field . widget . value_from_datadict ( self . data , self . files , prefixed_name )
[GROUND TRUTH]
# call the method field . widget . value_from_datadict with 3 arguments : self . data , self . files , prefixed_name , substitute the result for data_value .
[PREDICTED]
# call the method self . widget . widget with arguments : self . data , self . data , self . data , self . data , self . data , self . data ,

[INPUT]
return mark_safe ( force_text ( text ) . replace ( ' & ' , ' & amp ; ' ) . replace ( ' < ' , ' & lt ; ' ) . replace ( ' > ' , ' & gt ; ' ) . replace ( ' " ' , ' & quot ; ' ) . replace ( " ' " , ' & # 39 ; ' ) )
[GROUND TRUTH]
# call the function force_text with an argument text , replace every occurrence of ' & ' in the result with ' & amp ; ' ,
[PREDICTED]
# call the function ' with ' , ' ' ' & ' ' & ' and ' & ' & ' & ' & ' & ' ,

[INPUT]
lookups . appendlist ( name , ( new_matches , p_pattern + pat , dict ( defaults , * * pattern . default_kwargs ) ) )
[GROUND TRUTH]
# call the method lookups . appendlist with 2 arguments : name and a tuple containing 3 elements : new_matches , sum of p_pattern and pat ,
[PREDICTED]
# call the method lookups . appendlist with 2 arguments : result of the function dict . appendlist with 2 arguments :

[INPUT]
self . stdout . write ( " [ ] % s " % title )
[GROUND TRUTH]
# substitute ' % s ' with title in the string " [ ] % s " , write it to the standard output .
[PREDICTED]
# replace ' % s ' in string " [ % s " with title , write it to self . stdout .

[INPUT]
parser . add_argument ( ' --database ' , default = DEFAULT_DB_ALIAS , help = ' Nominates a database to print the SQL for . Defaults to the ' ' " default " database . ' )
[GROUND TRUTH]
# call the method parser . add_argument with 3 arguments : string ' --database ' , default set to DEFAULT_DB_ALIAS ,
[PREDICTED]
# call the method parser . add_argument with 3 arguments : string ' --database ' , default set to DEFAULT_DB_ALIAS ,

[INPUT]
link = cache_get ( key )
[GROUND TRUTH]
# call the function cache_get with an argument key , substitute the result for link .
[PREDICTED]
# call the function cache_get with an argument key , substitute the result for key .

[INPUT]
if not isinstance ( stream_or_string , ( bytes , six . string_types ) ) :
[GROUND TRUTH]
# if stream_or_string is not an instance of bytes or six . string_types ,
[PREDICTED]
# if if if if not is not an instance of six . string_types ,

[INPUT]
from django . conf import settings
[GROUND TRUTH]
# from django . conf import settings into default name space .
[PREDICTED]
# from django . conf import settings into default name space .

[INPUT]
return bool ( self . name )
[GROUND TRUTH]
# convert self . name into an boolean , return it .
[PREDICTED]
# convert self . name into boolean , return it .

[INPUT]
_ active . value = self . old_timezone
[GROUND TRUTH]
# substitute self . old_timezone for _ active . value .
[PREDICTED]
# substitute self . . . . . . . . .

[INPUT]
class EmailBackend ( BaseEmailBackend ) :
[GROUND TRUTH]
# derive the class EmailBackend from the BaseEmailBackend base class .
[PREDICTED]
# derive the class class from the BaseEmailBackend base class .

[INPUT]
check_for_migrations ( app_config , connection )
[GROUND TRUTH]
# call the function check_for_migrations with arguments app_config and connection .
[PREDICTED]
# call the function check_for_migrations with arguments : app_config and connection .

[INPUT]
setattr ( self . object , accessor_name , object_list )
[GROUND TRUTH]
# set accessor_name of the self . object to object_list .
[PREDICTED]
# set self . object attribute of the self . object object to self .

[INPUT]
def writer_leaves ( self ) :
[GROUND TRUTH]
# define the method writer_leaves with an argument self .
[PREDICTED]
# define the method writer_leaves with an argument self .

[INPUT]
for node in self . nodelist_loop :
[GROUND TRUTH]
# for every node in self . nodelist_loop ,
[PREDICTED]
# for every node in self . nodelist_loop ,

[INPUT]
except VariableDoesNotExist :
[GROUND TRUTH]
# if VariableDoesNotExist exception is caught ,
[PREDICTED]
# if VariableDoesNotExist exception is caught ,

[INPUT]
return True
[GROUND TRUTH]
# return boolean True .
[PREDICTED]
# return boolean True .

[INPUT]
return response
[GROUND TRUTH]
# return response .
[PREDICTED]
# return response .

[INPUT]
try :
[GROUND TRUTH]
# try ,
[PREDICTED]
# try ,

[INPUT]
path = os . environ . get ( ' PATH ' , '' ) . split ( os . pathsep )
[GROUND TRUTH]
# call the function os . environ . get with 2 arguments : string ' PATH ' and an empty string , split the result at the os . pathsep , substitute the result for path .
[PREDICTED]
# call the method os . get with 2 arguments : string ' PATH ' and os . path . split , substitute the result for path .

[INPUT]
try :
[GROUND TRUTH]
# binary or os . O_EXCL if allow_overwrite is boolean False , use the previous as the mode to open new_file_name file , assign the file descriptor to fd .   try ,
[PREDICTED]
# try ,

[INPUT]
exts = extensions if extensions else [ ' html ' , ' txt ' ]
[GROUND TRUTH]
# if extensions is false , substitute it for exts , otherwise exts is a list containing 2 elements : string ' html ' and string ' txt ' .
[PREDICTED]
# if extensions is true , substitute it for extensions , if not , extensions is an empty string .

[INPUT]
pad = b'= ' * ( - len ( s ) % 4 )
[GROUND TRUTH]
# calculate negative length of s , by modulus integer 4 , use the result as the number of ' = ' characters to be stored in pad .
[PREDICTED]
# subtract string ' < ( % ( ) ) ' , substitute it for pad .

[INPUT]
handler . addQuickElement ( " email " , item [ ' author_email ' ] )
[GROUND TRUTH]
# call the method handler . addQuickElement with 2 arguments : string ' email ' and value under the ' author_email ' key of the item dictionary .
[PREDICTED]
# call the method handler . addQuickElement with 2 arguments : string ' author_email ' and value under the ' email ' key of the item dictionary .

[INPUT]
reporter = ExceptionReporter ( request , is_email = True , * exc_info )
[GROUND TRUTH]
# and request_repr , respectively .   reporter is an instance of ExceptionReporter class , created with 3 arguments : request , is_email as boolean True ,
[PREDICTED]
# and re . VERBOSE , substitute the result for reporter .   call the function ExceptionReporter with 2 arguments : request and exc_info set to boolean True ,

[INPUT]
duplicate = super ( Context , self ) . _ _ copy _ _ ( )
[GROUND TRUTH]
# call the the method _ _ copy _ _ from the base class of the class Context , substitute the result for duplicate .
[PREDICTED]
# call the method _ _ _ _ _ from the base class of the class Context , substitute the result for duplicate .

[INPUT]
_ _ delitem _ _ = new_method_proxy ( operator . delitem )
[GROUND TRUTH]
# call the function new_method_proxy with an argument operator . delitem , substitute the result for _ _ delitem _ _ .
[PREDICTED]
# call the function new_method_proxy with an argument operator . delitem , substitute the result for _ _ _ _ _ .

[INPUT]
self . xml . startElement ( " object " , { } )
[GROUND TRUTH]
# call the method self . xml . startElement with argument string ' object ' and an empty dictionary .
[PREDICTED]
# call the method self . startElement with 2 arguments : string ' object ' and value under the ' object ' key of the self . xml .

[INPUT]
url = hashlib . md5 ( force_bytes ( iri_to_uri ( request . build_absolute_uri ( ) ) ) )
[GROUND TRUTH]
# call method request . build_absolute_uri , use the result as an argument for function call of iri_to_uri ,
[PREDICTED]
# call the method hashlib . md5 with an argument tuple with an element ,

[INPUT]
from django . core . management . base import BaseCommand , CommandError
[GROUND TRUTH]
# from django . core . management . base import BaseCommand and CommandError into default name space .
[PREDICTED]
# from django . base . base . base import import and CommandError into default name space .

[INPUT]
_ _ version _ _ = " 0 . 1 "
[GROUND TRUTH]
# _ _ version _ _ is a string " 0 . 1 " .
[PREDICTED]
# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ is a string " " .

[INPUT]
def strptime ( self , value , format ) :
[GROUND TRUTH]
# define the method strptime with arguments self , value and format .
[PREDICTED]
# define the method strptime with arguments self , value and format .

[INPUT]
class BaseTemporalField ( Field ) :
[GROUND TRUTH]
# derive the class BaseTemporalField from the base class Field class .
[PREDICTED]
# derive the class class from the base class Field class .

[INPUT]
class Command ( AppCommand ) :
[GROUND TRUTH]
# derive the class Command from the AppCommand base class .
[PREDICTED]
# derive class class from the AppCommand base class .

[INPUT]
self . use_tz = use_tz
[GROUND TRUTH]
# substitute use_tz for self . use_tz .
[PREDICTED]
# substitute use_tz for self . use_tz .

[INPUT]
if self . connector = = conn_type :
[GROUND TRUTH]
# if self . connector equals conn_type ,
[PREDICTED]
# if self . . equals to boolean False ,

[INPUT]
for member in members :
[GROUND TRUTH]
# for every member in members ,
[PREDICTED]
# for every member in members ,

[INPUT]
except IndexError :
[GROUND TRUTH]
# if IndexError exception is caught ,
[PREDICTED]
# if IndexError exception is caught ,

[INPUT]
try :
[GROUND TRUTH]
# try ,
[PREDICTED]
# try ,

[INPUT]
return " < DeserializedObject : % s . % s(pk=%s ) > " % ( self . object . _ meta . app_label , self . object . _ meta . object_name , self . object . pk )
[GROUND TRUTH]
# return a string " < DeserializedObject : % s . % s(pk=%s ) > " , where ' % s ' are replaced with self . object . _ meta . app_label ,
[PREDICTED]
# return a string " . % s . % s . % s . % s . % s . % s . % s " , where ' % s ' is replaced

[INPUT]
parser . add_argument ( ' --ipv6 ' , ' -6 ' , action = ' store_true ' , dest = ' use_ipv6 ' , default = False , help = ' Tells Django to use an IPv6 address . ' )
[GROUND TRUTH]
# call parser . add_argument method with ' --ipv6 ' , string ' -6 ' , action set to string ' store_true ' , dest set to string ' use_ipv6 ' ,
[PREDICTED]
# and help is a string ' Specifies the output to use when when the user for input of any kind . ' .   call the method parser . ' with ' % s

[INPUT]
if self . can_delete :
[GROUND TRUTH]
# label set to return value of the function _ called with an string ' Order ' and required as boolean False .   if self . can_delete is true ,
[PREDICTED]
# if self . . is true ,

[INPUT]
if len ( value ) ! = 2 :
[GROUND TRUTH]
# ' Use SplitDateTimeField instead . ' , RemovedInDjango19Warning and stacklevel set to integer 2 .   if length of value is not equal to integer 2 ,
[PREDICTED]
# if length of value is not equal to integer 1 ,

[INPUT]
help = ' Compiles . po files to . mo files for use with builtin gettext support . '
[GROUND TRUTH]
# help is string ' Compiles . po files to . mo files for use with builtin gettext support . ' .
[PREDICTED]
# help is a string ' Compiles . po files files files files files files files . . files . files files . . files . files files . . files . files files .

[INPUT]
mod_name , func_name = get_mod_func ( lookup_view )
[GROUND TRUTH]
# call the function get_mod_func with an argument lookup_view , store the result in mod_name and func_name , respectively .
[PREDICTED]
# call the function get_mod_func with an argument lookup_view , substitute the result for mod_name .

[INPUT]
if not unicodedata . combining ( char ) :
[GROUND TRUTH]
# call the method unicodedata . combining with an argument char , if it evaluates to false ,
[PREDICTED]
# call the method unicodedata . combining with an argument char , if it evaluates to false ,

[INPUT]
if sys . version_info [ 1 ] < = 1 :
[GROUND TRUTH]
# if second element of sys . version_info is smaller than or equal to integer 1 ,
[PREDICTED]
# if first element of sys . version_info is greater or equal to integer 1 ,

[INPUT]
def add_filters ( self , filterer , filters ) :
[GROUND TRUTH]
# define the method add_filters with 3 arguments : self , filterer and filters .
[PREDICTED]
# define the method add_filters with 3 arguments : self , filterer and filters .

[INPUT]
def wrapper ( * args ) :
[GROUND TRUTH]
# define the function wrapper with an argument unpacked list args .
[PREDICTED]
# define the function wrapper with an argument unpacked list args .

[INPUT]
from django . utils import six
[GROUND TRUTH]
# from django . utils import six into default name space .
[PREDICTED]
# from django . utils import six into default name space .

[INPUT]
sorted_items = sorted ( kwds . items ( ) )
[GROUND TRUTH]
# sort elements of kwds , substitute the result for sorted_items .
[PREDICTED]
# call the method sorted with an argument kwds , substitute the result for sorted_items .

[INPUT]
check_for_migrations ( app_config , connection )
[GROUND TRUTH]
# call the function check_for_migrations with an arguments app_config , connection .
[PREDICTED]
# call the function check_for_migrations with arguments : app_config and connection .

[INPUT]
if self . field . empty_label is not None :
[GROUND TRUTH]
# if self . field . empty_label is not None ,
[PREDICTED]
# if self . field . field is not None ,

[INPUT]
def f ( self ) :
[GROUND TRUTH]
# define the method f with an argument self .
[PREDICTED]
# define the method f with an argument self .

[INPUT]
from PIL import Image
[GROUND TRUTH]
# from PIL import Image into default namespace .
[PREDICTED]
# from PIL module import import

[INPUT]
return path , ''
[GROUND TRUTH]
# return path an an empty string .
[PREDICTED]
# return an empty string .

[INPUT]
prefix = settings . STATIC_URL
[GROUND TRUTH]
# substitute settings . STATIC_URL for prefix .
[PREDICTED]
# substitute settings . STATIC_URL for prefix .

[INPUT]
import copy
[GROUND TRUTH]
# import module copy .
[PREDICTED]
# copy .

[INPUT]
else :
[GROUND TRUTH]
# if not ,
[PREDICTED]
# if not ,

[INPUT]
MAXSIZE = int ( ( 1 < < 31 ) - 1 )
[GROUND TRUTH]
# bitwise shift integer 1 to the left by 31 spaces , substitute integer 1 from the result , convert the result to a integer , substitute it for MAXSIZE .
[PREDICTED]
# bitwise shift integer 1 to the left by integer 1 , substitute the result for MAXSIZE .

[INPUT]
raise TemplateSyntaxError ( " % r must be the first tag " " in the template . " % node )
[GROUND TRUTH]
# raise TemplateSyntaxError("%r must be the first tag in the template . " , where ' % s ' is replaced with node .
[PREDICTED]
# raise an r exception with an argument string " % r % r : % r " , where ' % s ' is replaced with the result of the function

[INPUT]
field_value = getInnerText ( node ) . strip ( )
[GROUND TRUTH]
# call the function getInnerText with an argument node , call the strip method on the result , substitute the result for field_value .
[PREDICTED]
# call the function getInnerText with an argument node , call the method strip on the result , substitute the result for field_value .

[INPUT]
self . username = settings . EMAIL_HOST_USER if username is None else username
[GROUND TRUTH]
# if username is None substitute settings . EMAIL_HOST_USER for self . username , if not substitute username for self . username .
[PREDICTED]
# if username is None substitute None for self . username , if not substitute username for self . username .

[INPUT]
if i > = self . initial_form_count ( ) and i > = self . min_num :
[GROUND TRUTH]
# if i is greater than , or equal to the result of the call to the method self . initial_form_count ,
[PREDICTED]
# if i is greater than or equal to self . initial_form_count ,

[INPUT]
return WidthRatioNode ( parser . compile_filter ( this_value_expr ) , parser . compile_filter ( max_value_expr ) , parser . compile_filter ( max_width ) , asvar = asvar )
[GROUND TRUTH]
# return an instance of a class WidthRatioNode , created with 4 arguments : result of the method parser . compile_filter ,
[PREDICTED]
# return an instance of parser class , created with 3 arguments : parser , parser . compile_filter ,

[INPUT]
return self . to + self . cc + self . bcc
[GROUND TRUTH]
# add together self . to , self . cc and self . bcc , return the result .
[PREDICTED]
# sum self . . . to self . to , return value of the self . to .

[INPUT]
return super ( QueryDict , self ) . popitem ( )
[GROUND TRUTH]
# call the method popitem from the base class of the class QueryDict , return the result .
[PREDICTED]
# call the method popitem from the base class of the class QueryDict , return the result .

[INPUT]
next = index + len ( self . _ boundary )
[GROUND TRUTH]
# sum index and length of self . _ boundary , substitute the result for next .
[PREDICTED]
# sum self . _ _ _ into a , and substitute it for self . _ _ .

[INPUT]
except ( DatabaseError , IntegrityError ) as e :
[GROUND TRUTH]
# if DatabaseError or IntegrityError , renamed to e , exceptions are caught ,
[PREDICTED]
# if DatabaseError or e , renamed to e , exception is caught ,

[INPUT]
from _ _ future _ _ import unicode_literals
[GROUND TRUTH]
# from _ _ future _ _ import unicode_literals into default name space .
[PREDICTED]
# from _ _ future _ _ import import into default name space .

[INPUT]
if isinstance ( choice_label , ( tuple , list ) ) :
[GROUND TRUTH]
# if choice_label is an instance of tuple or list ,
[PREDICTED]
# if tuple is an instance of tuple or tuple types ,

[INPUT]
for pattern in allowed_hosts :
[GROUND TRUTH]
# for every pattern in allowed_hosts :
[PREDICTED]
# for every pattern in allowed_hosts ,

[INPUT]
if processors is None :
[GROUND TRUTH]
# if processors is None ,
[PREDICTED]
# if if is None ,

[INPUT]
return settings . DEBUG
[GROUND TRUTH]
# return settings . DEBUG .
[PREDICTED]
# return settings . .

[INPUT]
return False
[GROUND TRUTH]
# return boolean True .
[PREDICTED]
# return boolean False .

[INPUT]
return False
[GROUND TRUTH]
# return boolean False .
[PREDICTED]
# return boolean False .

[INPUT]
else :
[GROUND TRUTH]
# if not ,
[PREDICTED]
# if not ,

[INPUT]
else :
[GROUND TRUTH]
# if not ,
[PREDICTED]
# if not ,

[INPUT]
try :
[GROUND TRUTH]
# try ,
[PREDICTED]
# try ,