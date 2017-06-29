[INPUT]
name = config . get ( ' name ' , '' )
[GROUND TRUTH]
# remove config dictionary element under ' name ' key , if it exists substitute it for name , if not , name is an empty string .
[PREDICTED]
# get the value under the ' name ' key of the options dictionary , if it exists substitute it for name , if not , name is None

[INPUT]
def run ( addr , port , wsgi_handler , ipv6 = False , threading = False ) :
[GROUND TRUTH]
# define the function run with 5 arguments : addr , port , wsgi_handler , ipv6 set to boolean False and threading set to boolean False .
[PREDICTED]
# define the function run with 4 arguments : port , port , port , port set to boolean False ,

[INPUT]
def date_format ( value , format = None , use_l10n = None ) :
[GROUND TRUTH]
# define the function date_format with 3 arguments : value , format set to None and use_l10n set to None .
[PREDICTED]
# define the function date_format with 3 arguments : value , value and format set to None .

[INPUT]
return property ( fget , fset , fdel , doc )
[GROUND TRUTH]
# return an property object with getter function fget , setter function fset , destructor fdel and documentation string doc .
[PREDICTED]
# return a tuple with 3 elements : fget , fset , fdel , fset , fset , fset , fset ,

[INPUT]
domains = ( ' djangojs ' , ' django ' )
[GROUND TRUTH]
# domains is a tuple with 2 elements : strings ' djangojs ' and ' django ' .
[PREDICTED]
# domains is a tuple with 2 elements : strings ' django ' and ' django ' .

[INPUT]
return self . nodelist_empty . render ( context )
[GROUND TRUTH]
# call the method self . nodelist_empty . render with an argument context , return the result .
[PREDICTED]
# call the method self . render . render with an argument context , return the result .

[INPUT]
value = formats . sanitize_separators ( value )
[GROUND TRUTH]
# call the method formats . sanitize_separators with an argument value , substitute the result for value .
[PREDICTED]
# call the method formats . sanitize_separators with an argument value , substitute the result for value .

[INPUT]
initial_prefixed_name = self . add_initial_prefix ( name )
[GROUND TRUTH]
# call the method self . add_initial_prefix with an argument name , substitute the result for initial_prefixed_name .
[PREDICTED]
# call the method self . add_initial_prefix with an argument name , substitute the result for initial_prefixed_name .

[INPUT]
def _ _ deepcopy _ _ ( self , memo ) :
[GROUND TRUTH]
# define the method _ _ deepcopy _ _ with 3 arguments : self and memo .
[PREDICTED]
# define the method _ _ deepcopy _ _ with 2 arguments : self and memo .

[INPUT]
def get_connection ( self , fail_silently = False ) :
[GROUND TRUTH]
# define the method get_connection with arguments self and fail_silently set to boolean False .
[PREDICTED]
# define the function get_connection with 2 arguments : self and fail_silently set to boolean False .

[INPUT]
sub_match_dict . update ( sub_match . kwargs )
[GROUND TRUTH]
# call the method sub_match_dict . update with an argument sub_match . kwargs .
[PREDICTED]
# call the method sub_match_dict . update with an argument sub_match . kwargs .

[INPUT]
from django . utils . itercompat import is_iterable
[GROUND TRUTH]
# from django . utils . itercompat import is_iterable into default name space .
[PREDICTED]
# from django . utils . utils import import into default name space .

[INPUT]
po_path = os . path . join ( dirpath , f )
[GROUND TRUTH]
# po_path is a string containing joined directory path from dirpath and f .
[PREDICTED]
# join join and f into a file path , substitute it for po_path .

[INPUT]
if self . verbosity > = 1 :
[GROUND TRUTH]
# if self . verbosity is greater or equal to integer 1 ,
[PREDICTED]
# if self . . is greater than integer 1 ,

[INPUT]
if os . fork ( ) > 0 :
[GROUND TRUTH]
# fork a child process , if the result equals integer 0 ,
[PREDICTED]
# if if file path exists ,

[INPUT]
self . can_read . acquire ( )
[GROUND TRUTH]
# call the method self . can_read . acquire .
[PREDICTED]
# call the method self . . . .

[INPUT]
self . keyOrder . append ( key )
[GROUND TRUTH]
# append key to self . keyOrder .
[PREDICTED]
# append key to self . keyOrder .

[INPUT]
str_number = str_number [ 1 : ]
[GROUND TRUTH]
# remove the first element from str_number .
[PREDICTED]
# substitute first element of str_number for str_number .

[INPUT]
return { }
[GROUND TRUTH]
# return an empty dictionary .
[PREDICTED]
# return an empty dictionary .

[INPUT]
return 12
[GROUND TRUTH]
# return integer 12 .
[PREDICTED]
# return 12 .

[INPUT]
warnings . warn ( " cache_choices has been deprecated and will be " " removed in Django 1 . 9 . " , RemovedInDjango19Warning , stacklevel = 2 )
[GROUND TRUTH]
# call the function warnings . warn with 3 arguments : string " cache_choices has been deprecated and will be removed in Django 1 . 9 . " ,
[PREDICTED]
# call the function warn with 3 arguments : string " cache_choices " has an and 1 and has an 1 " . "

[INPUT]
templatetags_modules_candidates + = [ ' % s . templatetags ' % app_config . name for app_config in apps . get_app_configs ( ) ]
[GROUND TRUTH]
# add string ' % s . templatetags ' to a list , where ' % s ' is replaced with app_config . name ,
[PREDICTED]
# append string ' % s . name ' to a list , append it to a list , append it to a list , append it to a list

[INPUT]
if not pythonrc :
[GROUND TRUTH]
# and string ' ~/ . pythonrc . py ' as tuples second element .   if pythonrc is true ,
[PREDICTED]
# if if is false ,

[INPUT]
super ( QueryDict , self ) . _ _ init _ _ ( )
[GROUND TRUTH]
# call the _ _ init _ _ method of the base class of the QueryDict class .
[PREDICTED]
# call the method _ _ init _ _ from the base class of the class QueryDict .

[INPUT]
pkg_name = ' templates/ ' + template_name
[GROUND TRUTH]
# concatenate string ' templates/ ' and template_name , substitute the result for pkg_name .
[PREDICTED]
# append ' template_name ' to it , substitute the result for pkg_name .

[INPUT]
return build_request_repr ( self )
[GROUND TRUTH]
# call the method build_request_repr with an argument self , return the result .
[PREDICTED]
# call the function build_request_repr with an argument self , return the result .

[INPUT]
if self . verbosity > = 1 :
[GROUND TRUTH]
# if self . verbosity is greater or equal than integer 1 ,
[PREDICTED]
# if self . . equals to integer 1 ,

[INPUT]
class SafeMIMEText ( MIMEMixin , MIMEText ) :
[GROUND TRUTH]
# derive the class SafeMIMEText from the MIMEMixin and MIMEText base class .
[PREDICTED]
# derive the class class from the MIMEMixin and MIMEText base class .

[INPUT]
if isinstance ( value , six . text_type ) :
[GROUND TRUTH]
# if value is an instance of six . text_type class ,
[PREDICTED]
# if if is an instance of value class ,

[INPUT]
package_path = package . _ _ path _ _
[GROUND TRUTH]
# substitute package . _ _ path _ _ for package_path .
[PREDICTED]
# substitute package_path . _ _ _ _ _ _ for _ _ .

[INPUT]
class EmailInput ( TextInput ) :
[GROUND TRUTH]
# derive the class EmailInput from the TextInput base class .
[PREDICTED]
# derive the class class from the TextInput base class .

[INPUT]
def write ( data ) :
[GROUND TRUTH]
# define the function write with an argument data .
[PREDICTED]
# define the function write with an argument data .

[INPUT]
httpd . daemon_threads = True
[GROUND TRUTH]
# httpd . daemon_threads is boolean True .
[PREDICTED]
# httpd . . is boolean True .

[INPUT]
except IndexError :
[GROUND TRUTH]
# if IndexError exception is caught ,
[PREDICTED]
# if IndexError exception is caught ,

[INPUT]
LOCK_SH = 0
[GROUND TRUTH]
# LOCK_SH is a integer 0 .
[PREDICTED]
# LOCK_SH is integer 0 .

[INPUT]
raise StopIteration ( )
[GROUND TRUTH]
# raise an StopIteration exception .
[PREDICTED]
# raise an StopIteration exception ,

[INPUT]
if inplural :
[GROUND TRUTH]
# if inplural is true ,
[PREDICTED]
# if if is true ,

[INPUT]
return
[GROUND TRUTH]
# return nothing .
[PREDICTED]
# return nothing .

[INPUT]
pass
[GROUND TRUTH]
# do nothing .
[PREDICTED]
# do nothing .

[INPUT]
pass
[GROUND TRUTH]
# do nothing .
[PREDICTED]
# do nothing .

[INPUT]
row = cursor . fetchone ( )
[GROUND TRUTH]
# substitute the ' % s ' with table and list containing key , respectively .   call the cursor . fetchone method , substitute the result for row .
[PREDICTED]
# call the method cursor . .

[INPUT]
defaults [ ' empty_permitted ' ] = True
[GROUND TRUTH]
# and i is greater than or equal to self . min_num ,   value under the ' empty_permitted ' key of the defaults dictionary is boolean True .
[PREDICTED]
# value under the ' empty_permitted ' key of the defaults dictionary is boolean True .

[INPUT]
self . lasttag = tag = match . group ( 1 ) . lower ( )
[GROUND TRUTH]
# find the first subgroup of the matched string from the match object , convert it to lowercase , substitute it for tag and self . lasttag .
[PREDICTED]
# call the method self . lower , with an argument , substitute the result for value under the ' . ' key of the self . _ lasttag .

[INPUT]
supported_platform = plat ! = ' Pocket PC ' and ( plat ! = ' win32 ' or ' ANSICON ' in os . environ )
[GROUND TRUTH]
# evaluate the logic expression , plat does not equals to string ' Pocket PC ' , and plat does not equals to string ' win32 '
[PREDICTED]
# if not ,

[INPUT]
raise ValueError ( " Invalid header : % r " % line )
[GROUND TRUTH]
# raise an ValueError with an argument string " Invalid header : % r " , where ' % s ' is replaced with line .
[PREDICTED]
# raise an ValueError exception with an argument string " Invalid header : % r " , where ' % s ' is replaced with line .

[INPUT]
from ctypes import ( sizeof , c_ulong , c_void_p , c_int64 , Structure , Union , POINTER , windll , byref )
[GROUND TRUTH]
# from ctypes import sizeof , c_ulong , c_void_p , c_int64 , Structure , Union , POINTER , windll and byref into default name space .
[PREDICTED]
# from , , , , , , , , , , , , , , , , , , , , , , , , , , , , ,

[INPUT]
if ( BLOCK_CONTEXT_KEY in render_context and render_context [ BLOCK_CONTEXT_KEY ] . get_block ( self . name ) is not None ) :
[GROUND TRUTH]
# if BLOCK_CONTEXT_KEY is contained in render_context and call to the method get_block with an argument self . name from the object ,
[PREDICTED]
# if BLOCK_CONTEXT_KEY is contained in self . name and render_context . name is not contained in BLOCK_CONTEXT_KEY ,

[INPUT]
register_to = kwargs . get ( ' register_to ' )
[GROUND TRUTH]
# get value under the ' register_to ' key of the kwargs dictionary , substitute it for register_to .
[PREDICTED]
# get the value under the ' register_to ' key of the options dictionary , substitute it for register_to .

[INPUT]
handler . addQuickElement ( " category " , cat )
[GROUND TRUTH]
# call the method handler . addQuickElement with 2 arguments : string ' category ' and cat .
[PREDICTED]
# call the method handler . addQuickElement with 2 arguments : string ' category ' and cat .

[INPUT]
def _ _ getattr _ _ ( self , name ) :
[GROUND TRUTH]
# define the method _ _ getattr _ _ with self and name as arguments .
[PREDICTED]
# define the method _ _ getattr _ _ with 2 arguments : self and name .

[INPUT]
return self . _ regex_dict [ language_code ]
[GROUND TRUTH]
# return the value under the language_code of the self . _ regex_dict dictionary .
[PREDICTED]
# return the value under the key key of the self . _ _ dictionary .

[INPUT]
name = self . path ( name )
[GROUND TRUTH]
# call the self . path with argument name , substitute it for name .
[PREDICTED]
# call the method self . path with an argument name , substitute the result for name .

[INPUT]
class datetime ( real_datetime ) :
[GROUND TRUTH]
# derive the class datetime from the real_datetime base class .
[PREDICTED]
# derive the class class from the real_datetime base class .

[INPUT]
extra_params = OrderedDict ( )
[GROUND TRUTH]
# extra_params is an instance of the class OrderedDict .
[PREDICTED]
# extra_params is an instance of OrderedDict class .

[INPUT]
return '' , ''
[GROUND TRUTH]
# return an empty string and an empty string .
[PREDICTED]
# return an empty string ,

[INPUT]
for dict _ in self . dicts :
[GROUND TRUTH]
# for every dict _ in self . dicts ,
[PREDICTED]
# for every _ in self . _ meta . dicts ,

[INPUT]
except ( ValueError , TypeError ) :
[GROUND TRUTH]
# if ValueError or TypeError exceptions are caught ,
[PREDICTED]
# if ValueError or TypeError exceptions are caught ,

[INPUT]
status_code = 500
[GROUND TRUTH]
# status_code is an integer 500 .
[PREDICTED]
# substitute status_code for status_code .

[INPUT]
break
[GROUND TRUTH]
# break the loop execution .
[PREDICTED]
# and unpacked dictionary kwargs , substitute the result for value .   try ,

[INPUT]
else :
[GROUND TRUTH]
# if not ,
[PREDICTED]
# if not ,

[INPUT]
raise ValueError ( ' Unable to add handler % r : % s ' % ( h , e ) )
[GROUND TRUTH]
# raise an ValueError exception with an argument string ' Unable to add handler % r : % s ' formated with h and e .
[PREDICTED]
# raise an ValueError exception with an argument string ' Unable add % r : % s ' formated with e .

[INPUT]
self . verbosity = int ( options . get ( ' verbosity ' ) )
[GROUND TRUTH]
# get the value under the key ' exclude ' of the options dictionary , convert it to an integer , substitute it for exclude .
[PREDICTED]
# convert self . verbosity into a string , substitute it for self . verbosity .

[INPUT]
data = data . replace ( microsecond = 0 )
[GROUND TRUTH]
# call the method data . replace with an argument microsecond set to integer 0 , substitute the result for data .
[PREDICTED]
# call the method data . replace with an argument microsecond set to integer 0 , substitute the result for data .

[INPUT]
def send_mail ( subject , message , from_email , recipient_list , fail_silently = False , auth_user = None , auth_password = None , connection = None , html_message = None ) :
[GROUND TRUTH]
# define send_mail funtion with subject , message , from_email , recipient_list , fail_silently set to boolean False ,
[PREDICTED]
# define the function , with 4 arguments : , set set to None , , set set to None ,

[INPUT]
self . _ wrapped = self . _ setupfunc ( )
[GROUND TRUTH]
# call the method self . _ setupfunc , substitute the result for self . _ wrapped .
[PREDICTED]
# call the method self . _ _ _ _ _ _ , substitute the result for self . _ _ wrapped .

[INPUT]
file = tempfile . NamedTemporaryFile ( suffix = ' . upload ' )
[GROUND TRUTH]
# call the method tempfile . NamedTemporaryFile with argument suffix set to string ' . upload ' .
[PREDICTED]
# call the method tempfile . NamedTemporaryFile with an argument string ' . ' , substitute the result for file .

[INPUT]
return import_string ( key_func )
[GROUND TRUTH]
# evaluate the function import_string with key_func as argument , return the result .
[PREDICTED]
# call the function import_string with an argument key_func , return the result .

[INPUT]
elif isinstance ( message , list ) :
[GROUND TRUTH]
# otherwise if message is an instance of the list type .
[PREDICTED]
# otherwise if message is an instance of message class ,

[INPUT]
self . _ stream = stream
[GROUND TRUTH]
# substitute stream for self . _ stream .
[PREDICTED]
# substitute stream for self . _ stream .

[INPUT]
request . resolver_match = resolver_match
[GROUND TRUTH]
# substitute resolver_match for request . resolver_match .
[PREDICTED]
# substitute resolver_match for request . resolver_match .

[INPUT]
with self . mutex :
[GROUND TRUTH]
# with self . mutex perform ,
[PREDICTED]
# self . mutex , renamed to self . stdout .

[INPUT]
except ValueError :
[GROUND TRUTH]
# if ValueError exception is caught ,
[PREDICTED]
# if ValueError exception is caught ,

[INPUT]
except IndexError :
[GROUND TRUTH]
# if IndexError exception is caught ,
[PREDICTED]
# if IndexError exception is caught ,

[INPUT]
except VariableDoesNotExist :
[GROUND TRUTH]
# if VariableDoesNotExist exception is caught ,
[PREDICTED]
# if VariableDoesNotExist exception is caught ,

[INPUT]
while bits :
[GROUND TRUTH]
# while bits is true ,
[PREDICTED]
# while bits is true ,

[INPUT]
raise ImportError
[GROUND TRUTH]
# raise an ImportError exception .
[PREDICTED]
# raise an exception .

[INPUT]
if path . isfile ( path_to_remove ) :
[GROUND TRUTH]
# if path_to_remove is file ,
[PREDICTED]
# if path ends with ' path_to_remove ' ,

[INPUT]
return False
[GROUND TRUTH]
# return boolean False .
[PREDICTED]
# return boolean False .

[INPUT]
import keyword
[GROUND TRUTH]
# import module keyword .
[PREDICTED]
# import module import module .

[INPUT]
return t
[GROUND TRUTH]
# return t .
[PREDICTED]
# return t .

[INPUT]
from django . template . smartif import IfParser , Literal
[GROUND TRUTH]
# validTemplateLibrary , BLOCK_TAG_START , BLOCK_TAG_END , VARIABLE_TAG_START , VARIABLE_TAG_END , SINGLE_BRACE_START , SINGLE_BRACE_END ,   COMMENT_TAG_START , COMMENT_TAG_END , VARIABLE_ATTRIBUTE_SEPARATOR , get_library , token_kwargs , kwarg_re and render_value_in_context .   from django . template . smartif import IfParser and Literal into default name space .
[PREDICTED]
# from django . template . template . template . smartif import Literal and Literal into default name space .

[INPUT]
self . _ regex_dict [ language_code ] = compiled_regex
[GROUND TRUTH]
# where ' % s ' is replace by regex and return value of the function six . text_type with an argument e .   substitute the compiled_regex for value under the language_code key of the self . _ regex_dict dictionary .
[PREDICTED]
# substitute language_code for value under the language_code key of the self . _ _ dictionary .

[INPUT]
table = connections [ db ] . ops . quote_name ( self . _ table )
[GROUND TRUTH]
# call the ops . quote_name method with argument self . _ table on the object under the db key of connections dictionary , substitute the result for table .
[PREDICTED]
# call the method ops . ops . _ ops . _ ops . _ ops . _ ops . _ meta . _ ops , use the result as an argument for the call to the self . _ .

[INPUT]
parser . add_library ( temp_lib )
[GROUND TRUTH]
# where ' % s ' is replaced with name and taglib .   call the method parser . add_library with an argument temp_lib .
[PREDICTED]
# call the method parser . add_library with an argument temp_lib .

[INPUT]
raise ContentNotRenderedError ( ' The response content must be ' ' rendered before it can be accessed . ' )
[GROUND TRUTH]
# raise an ContentNotRenderedError exception with an sring ' The response content must be rendered before it can be accessed . ' .
[PREDICTED]
# raise an ContentNotRenderedError exception with an argument string ' The The The response be be be be be be be be be be be be be be be be be be be be be be be be be be be be be be be be be

[INPUT]
app_config = apps . get_app_config ( app_label )
[GROUND TRUTH]
# call the method apps . get_app_config with an argument app_label , substitute the result for app_config .
[PREDICTED]
# call the method apps . get_app_config with an argument app_label , substitute the result for app_config .

[INPUT]
logging . _ handlers . clear ( )
[GROUND TRUTH]
# disable_existing is boolean True .   call the method logging . _ handler . clear .
[PREDICTED]
# call the method logging . _ _ . _ _ . _ _ . _ _ . _ _ . _ _ . _ _ . _ _ . _ _ . _ _ . _ _ . _ _ . _ _ . _ _

[INPUT]
from django . db . models . fields . related import RelatedObject
[GROUND TRUTH]
# from django . db . models . fields . related import RelatedObject into default namespace .
[PREDICTED]
# from django . db . models . models . models . models . models . models . models . models . models . models . models . models . models . models . models . models . models . models . models . models . models

[INPUT]
elif isinstance ( timezone , six . string_types ) and pytz is not None :
[GROUND TRUTH]
# otherwise if timezone is an instance of six . string_types and pytz is not None ,
[PREDICTED]
# otherwise if six . string_types is not an instance of six . string_types and six . string_types is not equal to a string " pytz six " ,

[INPUT]
@ property
[GROUND TRUTH]
# return boolean True , otherwise return boolean False .   property decorator .
[PREDICTED]
# property decorator ,

[INPUT]
def root_attributes ( self ) :
[GROUND TRUTH]
# define the method root_attributes with an argument self .
[PREDICTED]
# define the method root_attributes with an argument self .

[INPUT]
def decorating_function ( user_function ) :
[GROUND TRUTH]
# define the function decorating_function with an argument user_function .
[PREDICTED]
# define the function decorating_function with an argument user_function .

[INPUT]
def encoding ( self ) :
[GROUND TRUTH]
# define the method encoding with an argument self .
[PREDICTED]
# define the method encoding with an argument self .

[INPUT]
forms_to_delete = self . deleted_forms
[GROUND TRUTH]
# substitute self . deleted_forms for forms_to_delete .
[PREDICTED]
# substitute self . . for forms_to_delete .

[INPUT]
for bit in self . lookups :
[GROUND TRUTH]
# for bit in self . lookups ,
[PREDICTED]
# for every bit in self . lookups ,

[INPUT]
except TypeError :
[GROUND TRUTH]
# if TypeError exception is caught ,
[PREDICTED]
# if TypeError exception is caught ,

[INPUT]
for model in model_list :
[GROUND TRUTH]
# for every model in model_list ,
[PREDICTED]
# for every model in model_list ,

[INPUT]
for template_dir in template_dirs :
[GROUND TRUTH]
# for every template_dir in template_dirs ,
[PREDICTED]
# for every template_dir in template_dirs ,

[INPUT]
if primary_keys :
[GROUND TRUTH]
# if primary_keys is true ,
[PREDICTED]
# if if is true ,

[INPUT]
try :
[GROUND TRUTH]
# try ,
[PREDICTED]
# try ,

[INPUT]
_ html_parser . HTMLParser . _ _ init _ _ ( self , convert_charrefs = convert_charrefs , * * kwargs )
[GROUND TRUTH]
# and dictionary of arbitrary length * * kwargs as arguments .   call the initialization method for the base class , _ html_parser . HTMLParser . _ _ init _ _ with self ,
[PREDICTED]
# and unpacked dictionary kwargs .   call the method parser . _ _ init _ _ with 3 arguments : self , convert_charrefs and unpacked dictionary kwargs .

[INPUT]
sql , references = connection . creation . sql_create_model ( model , no_style ( ) , seen_models )
[GROUND TRUTH]
# app_name and model . _ meta . object_name , respectively .   evaluate connection . creation . sql_create_model method with model , no_style ( ) and seen_models as arguments ,
[PREDICTED]
# and include_auto_created set to boolean True ,   call the method connection . creation . creation . creation . creation . creation . creation . creation . creation . creation . creation . creation .

[INPUT]
raise ValidationError ( self . error_messages [ ' required ' ] , code = ' required ' )
[GROUND TRUTH]
# raise an ValidationError with 2 arguments : value under the ' required ' key of the self . error_messages dictionary and code set to ' required ' .
[PREDICTED]
# raise an ValidationError with 2 arguments : value under the ' required ' key of the self . error_messages dictionary and code set to ' required ' .

[INPUT]
def _ _ init _ _ ( self , max_length = None , min_length = None , * args , * * kwargs ) :
[GROUND TRUTH]
# define the method _ _ init _ _ with 5 arguments : self , max_length set to None , min_length set to None , unpacked list args ,
[PREDICTED]
# define the method _ _ init _ _ with 4 arguments : self , max_length set to None , unpacked list args ,

[INPUT]
raise MultiPartParserError ( ' multipartparser . exhaust ( ) was passed a non - iterable or stream parameter ' )
[GROUND TRUTH]
# raise an MultiPartParserError with an argument string ' multipartparser . exhaust ( ) was passed a non - iterable or stream parameter ' .
[PREDICTED]
# raise an exhaust with an argument string ' multipartparser multipartparser - multipartparser - - multipartparser - - - - - - - - - - - - - - - - - - - -

[INPUT]
nm = Header ( nm , encoding ) . encode ( )
[GROUND TRUTH]
# call the encode function on the Header class instance , created with arguments nm and encoding , substitute the result for nm .
[PREDICTED]
# call the method Header with 2 arguments : nm and encoding , substitute the result for nm .

[INPUT]
def _ _ init _ _ ( self , producer , length = None ) :
[GROUND TRUTH]
# define the method _ _ init _ _ with 3 arguments : self , producer and length set to None .
[PREDICTED]
# define the method _ _ init _ _ with 4 arguments : self , producer and length set to None .

[INPUT]
migration = executor . loader . get_migration_by_prefix ( app_label , migration_name )
[GROUND TRUTH]
# call the executor . loader . get_migration_by_prefix with app_label and migration_name with arguments , substitute the result fr migration .
[PREDICTED]
# call the method executor . loader . loader with an argument app_label , substitute the result for migration .

[INPUT]
if module_has_submodule ( app_config . module , module_to_search ) :
[GROUND TRUTH]
# if call to the function module_has_submodule with 2 arguments : app_config . module and module_to_search evaluates to true ,
[PREDICTED]
# call the function module_has_submodule with 2 arguments : app_config and module_to_search .

[INPUT]
while self . exists ( name ) :
[GROUND TRUTH]
# as long as self . exists function with argument name evaluates to boolean True ,
[PREDICTED]
# call the method self . exists with argument name , substitute it for name .

[INPUT]
def render_value_in_context ( value , context ) :
[GROUND TRUTH]
# define the function render_value_in_context with 2 arguments : value and context .
[PREDICTED]
# define the function render_value_in_context with 2 arguments : value and context .

[INPUT]
def tzname ( self , dt ) :
[GROUND TRUTH]
# define the method tzname with 2 arguments : self and dt .
[PREDICTED]
# define the method tzname with 2 arguments : self and dt .

[INPUT]
class RawPostDataException ( Exception ) :
[GROUND TRUTH]
# derive the class RawPostDataException from the base class Exception .
[PREDICTED]
# derive the class class from the Exception base class .

[INPUT]
except smtplib . SMTPException :
[GROUND TRUTH]
# if smtplib . SMTPException exception is caught ,
[PREDICTED]
# if smtplib . . is true ,

[INPUT]
if not self . is_bound :
[GROUND TRUTH]
# if self . is_bound is false ,
[PREDICTED]
# if self . is_bound is false ,

[INPUT]
self . is_reversed = is_reversed
[GROUND TRUTH]
# substitute is_reversed for self . is_reversed .
[PREDICTED]
# substitute is_reversed for self . is_reversed .

[INPUT]
name = content . name
[GROUND TRUTH]
# substitute content . name for name .
[PREDICTED]
# substitute name . name for name .

[INPUT]
outdict = { }
[GROUND TRUTH]
# outdict is an empty dictionary .
[PREDICTED]
# outdict is an empty dictionary .

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
for opt in [ ' fields ' , ' exclude ' , ' localized_fields ' ] :
[GROUND TRUTH]
# assign the result to opts and new_class . _ meta .   for every opt in list containing 3 elements : strings ' fields ' , ' exclude ' and ' localized_fields ' ,
[PREDICTED]
# for every opt and value in return value of the function six . ' called with 3 arguments : string ' exclude ' ,

[INPUT]
MAXSIZE = int ( ( 1 < < 63 ) - 1 )
[GROUND TRUTH]
# bitwise shift integer 1 to the left by 63 spaces , substitute integer 1 from the result , convert the result to a integer , substitute it for MAXSIZE .
[PREDICTED]
# convert first element of < to integer 1 , substitute it for MAXSIZE .

[INPUT]
_ _ all _ _ = [ ' UploadFileException ' , ' StopUpload ' , ' SkipFile ' , ' FileUploadHandler ' , ' TemporaryFileUploadHandler ' , ' MemoryFileUploadHandler ' , ' load_handler ' , ' StopFutureHandlers ' ]
[GROUND TRUTH]
# _ _ all _ _ is a string containing strings : ' UploadFileException ' , ' StopUpload ' , ' SkipFile ' , ' FileUploadHandler ' ,
[PREDICTED]
# _ _ ' _ _ is a list containing 4 initial entries : ' ' ' , ' ' , ' ' , ' ' , ' ' , ' ' ' ,

[INPUT]
xreadlines = property ( lambda self : self . file . xreadlines )
[GROUND TRUTH]
# define lambda function that returns self . file . xreadlines field , use it as an argument for property function , put the result in xreadlines .
[PREDICTED]
# define lambda function that returns self . xreadlines . xreadlines field , use it as an argument for the call to the function property ,

[INPUT]
UnicodeDecodeError . _ _ init _ _ ( self , * args )
[GROUND TRUTH]
# call the initialization method UnicodeDecodeError . _ _ init _ _ , with self instance of this class and * args as arguments .
[PREDICTED]
# call the method _ _ init _ _ with 2 arguments : self and unpacked list args .

[INPUT]
upto = start
[GROUND TRUTH]
# tuple with 2 elements : upto and start and boolean False , append the result to result .   substitute start for upto .
[PREDICTED]
# upto is an integer 0 .

[INPUT]
def set_many ( self , data , timeout = DEFAULT_TIMEOUT , version = None ) :
[GROUND TRUTH]
# define the method set_many with self , data , timeout set to DEFAULT_TIMEOUT and version set to None as arguments .
[PREDICTED]
# define the method set_many with 4 arguments : self , data , data set to None and version set to None .

[INPUT]
return apps . get_model ( model_identifier )
[GROUND TRUTH]
# call the method apps . get_model with an argument model_identifier , return the result .
[PREDICTED]
# call the method apps . get_model with an argument model_identifier , return the result .

[INPUT]
shutil . copymode ( old_path , new_path )
[GROUND TRUTH]
# call the function shutil . copymode with arguments old_path and new_path .
[PREDICTED]
# call the function shutil . copymode with arguments old_path and new_path .

[INPUT]
if not value and self . required :
[GROUND TRUTH]
# if value is false and self . required is true ,
[PREDICTED]
# if self does nt have an attribute ' and ' are not contained in self . required .

[INPUT]
from django . utils import six
[GROUND TRUTH]
# from django . utils import six into default name space .
[PREDICTED]
# from django . utils import six into default name space .

[INPUT]
elif name is not None and filter_func is None :
[GROUND TRUTH]
# otherwise if name is not None and filter_func is None ,
[PREDICTED]
# otherwise if name is not None and and is not None ,

[INPUT]
class StopUpload ( UploadFileException ) :
[GROUND TRUTH]
# derive the class StopUpload from the UploadFileException base class .
[PREDICTED]
# derive the class class from the UploadFileException base class .

[INPUT]
words = words [ : length ]
[GROUND TRUTH]
# substitute first length elements of words for words .
[PREDICTED]
# substitute first element of words for words .

[INPUT]
except SuspiciousOperation as e :
[GROUND TRUTH]
# if exception SuspiciousOperation as e is caught ,
[PREDICTED]
# if e , renamed to e , exception is caught ,

[INPUT]
self . old_method_name = old_method_name
[GROUND TRUTH]
# substitute old_method_name for self . old_method_name .
[PREDICTED]
# substitute old_method_name for self . old_method_name .

[INPUT]
if pickled is not None :
[GROUND TRUTH]
# if pickled is not None .
[PREDICTED]
# if if not None is None ,

[INPUT]
app_list_value . append ( model )
[GROUND TRUTH]
# append model to app_list_value .
[PREDICTED]
# append model to app_list_value .

[INPUT]
if is_templatized :
[GROUND TRUTH]
# if is_templatized is true ,
[PREDICTED]
# if if is true ,

[INPUT]
import contextlib
[GROUND TRUTH]
# import module contextlib .
[PREDICTED]
# import module import module .

[INPUT]
def as_json ( self , escape_html = False ) :
[GROUND TRUTH]
# for every f and e in list of tuples of self dictionary key , pair entries .   define the method as_json with 2 argumens self and escape_html set to boolean False .
[PREDICTED]
# define the method as_json with 2 arguments : self and escape_html set to boolean False .

[INPUT]
return base64 . urlsafe_b64encode ( s ) . rstrip ( b'\n= ' )
[GROUND TRUTH]
# call the method base64 . urlsafe_b64encode with an argument s , strip the result of the bytes string ' \n= ' from the right , return it .
[PREDICTED]
# call the method base64 . rstrip with an argument string ' b'\n= ' , return the result .

[INPUT]
message = ungettext_lazy ( ' Ensure this value has at most % ( limit_value)d character ( it has % ( show_value)d ) . ' , ' Ensure this value has at most % ( limit_value)d characters ( it has % ( show_value)d ) . ' , ' limit_value ' )
[GROUND TRUTH]
# call the function ungettext_lazy with 3 arguments : string ' Ensure this value has at most % ( limit_value)d character ( it has % ( show_value)d ) ,
[PREDICTED]
# call the function ungettext_lazy with 3 arguments : string ' Ensure this this has ' , string ' Ensure this this has ' ,

[INPUT]
return getattr ( self , _ assertRaisesRegex ) ( * args , * * kwargs )
[GROUND TRUTH]
# get _ assertRaisesRegex attribute of the self object , call the result with 2 arguments : unpacked list args ,
[PREDICTED]
# get the attribute ' from ' of the self object , if it exists return it , if not , call the method self . assertRaisesRegex ,

[INPUT]
else :
[GROUND TRUTH]
# string joined from invalided_apps list and separated with string ' , ' .   if not ,
[PREDICTED]
# if not ,

[INPUT]
return escape ( value )
[GROUND TRUTH]
# call the function escape with an argument value , return the result .
[PREDICTED]
# call the function escape with an argument value , return the result .

[INPUT]
match = datetime_re . match ( value )
[GROUND TRUTH]
# match regex datetime_re with value , substitute the result for match .
[PREDICTED]
# call the method datetime_re . match with an argument value , substitute the result for match .

[INPUT]
def add_arguments ( self , parser ) :
[GROUND TRUTH]
# define the method add_arguments with self and parser as arguments .
[PREDICTED]
# define the method add_arguments with 2 arguments self and parser .

[INPUT]
def _ unpack_ipv4 ( ip_str ) :
[GROUND TRUTH]
# define the function _ unpack_ipv4 with an argument ip_str .
[PREDICTED]
# define the function _ _ unpack_ipv4 with an argument ip_str .

[INPUT]
except OSError as e :
[GROUND TRUTH]
# if OSError , renamed to e , is caught ,
[PREDICTED]
# if e , renamed to e , exception is caught ,

[INPUT]
if len ( bits ) > 2 :
[GROUND TRUTH]
# if length of bits is greater than integer 2 ,
[PREDICTED]
# if length of 2 is greater than integer 1 and length of 2 is equal to integer 2 ,

[INPUT]
def get_default_prefix ( cls ) :
[GROUND TRUTH]
# define the method get_default_prefix with an argument cls .
[PREDICTED]
# define the function get_default_prefix with an argument cls .

[INPUT]
def force_escape ( value ) :
[GROUND TRUTH]
# define the function force_escape with an argument value .
[PREDICTED]
# define the function force_escape with an argument value .

[INPUT]
from django . conf . locale import LANG_INFO
[GROUND TRUTH]
# from django . conf . locale import LANG_INFO .
[PREDICTED]
# from django . locale . locale import import into default name space .

[INPUT]
except ( OSError , IOError ) :
[GROUND TRUTH]
# if OSError or IOError exceptions were raised ,
[PREDICTED]
# if IOError or IOError exceptions are caught ,

[INPUT]
if mem_args in cache :
[GROUND TRUTH]
# if mem_args is contained in cache ,
[PREDICTED]
# if if if mem_args is contained in cache ,

[INPUT]
self . params = params
[GROUND TRUTH]
# substitute params for self . params .
[PREDICTED]
# substitute params for self . params .

[INPUT]
if offset is not None :
[GROUND TRUTH]
# if offset is not None ,
[PREDICTED]
# if if not None is None ,

[INPUT]
raise StopIteration ( )
[GROUND TRUTH]
# raise an StopIteration exception .
[PREDICTED]
# raise an StopIteration exception ,

[INPUT]
message_context = None
[GROUND TRUTH]
# message_context is None .
[PREDICTED]
# message_context is None .

[INPUT]
self . is_bound = data is not None or files is not None
[GROUND TRUTH]
# if data is not None or files is not None , self . is_bound is boolean True , otherwise it is boolean False .
[PREDICTED]
# if self . is_bound is not None ,

[INPUT]
raise NotImplementedError ( ' subclasses of BaseCache must provide an add ( ) method ' )
[GROUND TRUTH]
# raise an exception of class NotImplementedError with string ' subclasses of BaseCache must provide an add ( ) method ' as argument .
[PREDICTED]
# raise an NotImplementedError exception with an argument string ' subclasses of of of of of of of of of of of of of of of

[INPUT]
key = self . make_key ( key , version = version )
[GROUND TRUTH]
# call the method self . make_key with key and version set to version as arguments , substitute it for key .
[PREDICTED]
# call the method self . make_key with version set to version as arguments , substitute the result for key .

[INPUT]
with transaction . atomic ( using = self . using ) :
[GROUND TRUTH]
# call the method transaction . atomic with an argument using set to self . using , with the result ,
[PREDICTED]
# call the method transaction . atomic with an argument self . using , for every using in result ,

[INPUT]
localedir = os . path . join ( app_config . path , ' locale ' )
[GROUND TRUTH]
# join app_config . path and string ' locale ' into a file path , substitute it for localedir .
[PREDICTED]
# path is a tuple with 2 elements : strings ' . ' and ' . ' .

[INPUT]
for match in tag_re . finditer ( self . template_string ) :
[GROUND TRUTH]
# call the method tag_re . finditer with an argument self . template_string , for every match in result ,
[PREDICTED]
# call the method self . finditer with an argument self . template_string , for every match in the result ,

[INPUT]
return value . replace ( " " , " \xa0 " )
[GROUND TRUTH]
# replace every occurrence of ' ' in value for ' \xa0 ' , return the result .
[PREDICTED]
# call the method value . replace with an argument string ' \xa0 \xa0 ' , return the result .

[INPUT]
for f in opts . many_to_many + opts . virtual_fields :
[GROUND TRUTH]
# append opts . virtual_fields to opts . many_to_many , for every f in the result ,
[PREDICTED]
# for every opts in opts . many_to_many ,

[INPUT]
block_context . add_blocks ( self . blocks )
[GROUND TRUTH]
# call the method block_context . add_blocks with an argument self . block .
[PREDICTED]
# call the method block_context . add_blocks with an argument self . blocks .

[INPUT]
if self . verbosity > 1 :
[GROUND TRUTH]
# if self . verbosity is greater than integer 1 ,
[PREDICTED]
# if self . . is greater than integer 1 ,

[INPUT]
if self . field . empty_label is not None :
[GROUND TRUTH]
# if self . field . empty_label is not None ,
[PREDICTED]
# if self . field . field . field is not None ,

[INPUT]
if key_func is not None :
[GROUND TRUTH]
# if key_func is not of None type ,
[PREDICTED]
# if if not None is None ,

[INPUT]
raise self . exception
[GROUND TRUTH]
# raise an self . exception exception .
[PREDICTED]
# self . exception is boolean True .

[INPUT]
if app_config . models_module is None :
[GROUND TRUTH]
# if app_config . models_module is None ,
[PREDICTED]
# if if . models_module is None ,

[INPUT]
except ImportError :
[GROUND TRUTH]
# if ImportError exception is caught ,
[PREDICTED]
# if ImportError exception is caught ,

[INPUT]
res = ''
[GROUND TRUTH]
# res is an empty string .
[PREDICTED]
# res is an empty string .

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
return maybe
[GROUND TRUTH]
# return maybe .
[PREDICTED]
# return maybe .

[INPUT]
sql . extend ( connection . creation . sql_for_pending_references ( model , no_style ( ) , pending_references ) )
[GROUND TRUTH]
# use the result as the argument for the call to the sql . extend method .   call the connection . creation . sql_for_pending_references method with refto , no_style ( ) and pending_references as arguments ,
[PREDICTED]
# and include_auto_created set to boolean True ,   call the method connection . extend with 2 arguments : model and pending_references ,

[INPUT]
raise ValueError ( " make_aware expects a naive datetime , got % s " % value )
[GROUND TRUTH]
# raise an ValueError exception with an argument string " make_aware expects a naive datetime , got % s " , where ' % s ' is replaced with value .
[PREDICTED]
# raise an ValueError exception with an argument string " make_aware expects expects expects expects expects expects expects a a a a a a a a a a a a % r " , where ' % s

[INPUT]
members = [ member for member in self . _ archive . getmembers ( ) if member . name ! = ' pax_global_header ' ]
[GROUND TRUTH]
# members is a list with elements member for every member in the result of the function self . _ archive . getmembers ,
[PREDICTED]
# for every member in self . _ _ archive . _ meta . _ _ archive _ _ , append tuple containing a string ' pax_global_header ' .

[INPUT]
key = self . make_key ( key , version = version )
[GROUND TRUTH]
# call the method self . make_key with key and version set to version as arguments , substitute it for key .
[PREDICTED]
# call the method self . make_key with version set to version as arguments , substitute the result for key .

[INPUT]
stream_or_string = stream_or_string . decode ( ' utf-8 ' )
[GROUND TRUTH]
# call the method stream_or_string . decode with an argument string ' utf-8 ' , substitute the result for stream_or_string .
[PREDICTED]
# call the method stream_or_string . decode with an argument string ' utf-8 ' , substitute the result for stream_or_string .

[INPUT]
for option in option_label :
[GROUND TRUTH]
# called with an argument option_value , append the result to output .   for every option in option_label ,
[PREDICTED]
# for every option in option_label ,

[INPUT]
ch , escaped = next ( pattern_iter )
[GROUND TRUTH]
# get the next element of the iterable pattern_iter , assign the result for ch and escaped , respectively .
[PREDICTED]
# get the next element of the iterable pattern_iter , assign the result for ch and pattern_iter .

[INPUT]
value = self . _ resolve_lookup ( context )
[GROUND TRUTH]
# call the function self . _ resolve_lookup with an argument context , substitute the result for value .
[PREDICTED]
# call the method self . _ _ with an argument value , substitute the result for value .

[INPUT]
msg = self . style . HTTP_NOT_FOUND ( msg )
[GROUND TRUTH]
# call the self . style . HTTP_NOT_FOUND with an argument msg , substitute it for msg .
[PREDICTED]
# call the method self . style . style with an argument msg , substitute it for msg .

[INPUT]
matches = filter_re . finditer ( token )
[GROUND TRUTH]
# call the method filter_re . finditer with an argument token , substitute the result for matches .
[PREDICTED]
# call the method filter_re . finditer with an argument token , substitute the result for matches .

[INPUT]
from django . utils . http import urlquote
[GROUND TRUTH]
# from django . utils . http import urlquote into default name space .
[PREDICTED]
# from django . utils . utils import import into default name space .

[INPUT]
return force_text ( url )
[GROUND TRUTH]
# call the function force_text with an argument url , return the result .
[PREDICTED]
# call the function force_text with an argument url , return the result .

[INPUT]
def validate_unique ( self ) :
[GROUND TRUTH]
# define the method validate_unique with an argument self .
[PREDICTED]
# define the method validate_unique with an argument self .

[INPUT]
def iriencode ( value ) :
[GROUND TRUTH]
# define the function iriencode with an argument value .
[PREDICTED]
# define the function iriencode with an argument value .

[INPUT]
opts = instance . _ meta
[GROUND TRUTH]
# substitute instance . _ meta for opts .
[PREDICTED]
# substitute opts . _ meta for opts .

[INPUT]
self . mod = old
[GROUND TRUTH]
# substitute old for self . mod .
[PREDICTED]
# substitute old for self . old .

[INPUT]
values = reversed ( values )
[GROUND TRUTH]
# reverse elements order of values .
[PREDICTED]
# call the function reversed with an argument values , substitute the result for values .

[INPUT]
if as_form :
[GROUND TRUTH]
# if as_form is true ,
[PREDICTED]
# if if is true ,

[INPUT]
return
[GROUND TRUTH]
# return nothing .
[PREDICTED]
# return nothing .

[INPUT]
try :
[GROUND TRUTH]
# try ,
[PREDICTED]
# try ,