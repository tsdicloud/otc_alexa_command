# __init__.py - Starting of our application  
from flask       import Flask, request
from flask_ask   import Ask, statement, question, request as ask_request  
from flask_babel import Babel, gettext
from babel.core  import negotiate_locale

from otc_service import simple_os_queries  
#from OpenSSL import SSL
  
# Initialize Flask  
app = Flask(__name__)  
app.config.from_pyfile('app.config')

# Initialize Flask Ask and assign URL  
ask   = Ask(app, "/otc_control")  
babel = Babel(app)

# implement language matching method for alexa requests
@babel.localeselector
def get_current_locale():
    if hasattr(ask_request, 'locale'):
        #preferred = [x.replace('-', '_') for x in ask_request.locale.values()]
        preferred = [ ask_request.locale.replace('-', '_')]
    else:
        preferred = [app.config['BABEL_DEFAULT_LOCALE']]
    language = negotiate_locale(preferred, app.config['BABEL_ASK_LOCALES'])
    app.logger.debug("Selected language={}".format(language))
    app.logger.debug(app.config['BABEL_TRANSLATION_DIRECTORIES'])
    return language

#@app.before_request
#def before():
#    app.logger.debug(request.headers)
#    app.logger.debug(request.get_data(as_text=True))

# Set a useful response for the root  
@app.route('/')  
def homepage():  
    return "Open Telekom Cloud Control Alexa Skill"  

@app.route("/alive")
def alive_check():
    return "OtcControlLive", 200
  
# Set a welcome message when the skill is started  
@ask.launch  
def start_skill():  
    welcome_message = gettext('online')  
    return question(welcome_message)  
  
# Define our intent and query the backend  
@ask.intent("VMCountIntent")  
def vm_count():  
    count = simple_os_queries.vm_count()  
    count_msg = gettext('servers {total}, running {run}, stopped {stopped}').format(total=count[0],run=count[1], stopped=count[2]).encode('utf-8')
    return statement(count_msg)

@ask.intent("VolCountIntent")
def vol_count():
    volsize = simple_os_queries.total_volume_size()
    volsize_msg = gettext('{num} volumes, {size} size, {unused} unused').format(num=volsize[0],size=volsize[1],unused=volsize[2]).encode('utf-8')
    return statement(volsize_msg)

# Define shutdown message  
@ask.intent("AMAZON.StopIntent")
@ask.intent("AMAZON.CancelIntent")
def shutdown():
    bye_text=gettext("Bye").encode('utf-8')
    return statement(bye_text)
 
@ask.intent('BestCloud')  
def bestcloud(dummy):  
    best_text = gettext('The best cloud').encode('utf-8') 
    return statement(best_text)  

@ask.intent('Cloudifier')  
def cloudifier(dummy):  
    best_text = gettext('Cloudifier').encode('utf-8')  
    return statement(best_text)  

@ask.intent('MultiCloud')  
def multicloud(dummy):  
    text = gettext('MultiCloud').encode('utf-8')  
    return statement(text) 

@ask.intent('Digital')  
def digital(dummy):
    text = gettext('Digital')
    return statement(text) 

@ask.intent('DevOps')  
def devops(dummy):  
    text = gettext('DevOps').encode('utf-8')  
    return statement(text) 

@ask.intent('DevOpsService')  
def devopsaas(dummy):  
    text = gettext('DevOpsService').encode('utf-8')  
    return statement(text) 

@ask.intent('TalkPrinciples')  
def talkprinciples(dummy):  
    text = gettext('TalkPrinciples').encode('utf-8')  
    return statement(text) 

@app.route('/<path:dummy>')  
def fallback(dummy):  
    uups_text = gettext('Uups').encode('utf-8')  
    return statement(uups_text)  

# Main function  
if __name__ == '__main__':  

    # for direct ssl testing
    # context =('alexa_otc.crt','alexa_otc.key')
    # app.run(host='0.0.0.0', port=5443,ssl_context=context,debug=True) 
    #app.run(host='0.0.0.0', port=5443,debug=True) 
    app.run(host='0.0.0.0', port=5443,debug=True) 
