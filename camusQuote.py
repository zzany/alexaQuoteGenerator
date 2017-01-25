
from __future__ import print_function
import random

# ------------------------------- Quotes ---------------------------------------

quote1 =    """ Don't walk in front of me, I may not follow.
                Don't walk behind me, I may not lead. Walk beside me,
                just be my friend. """

quote2 =    """ You will never be happy if you continue to search
                for what happiness consists of. You will never live
                if you are looking for the meaning of life """

quote3 =    """ In the depth of winter, I finally learned that within me there
                lay an invincible summer. """
                
quote4 =    """ Man is the only creature who refuses to be what he is """

quote5 =    """ Nobody realizes that some people expend tremendous
                energy merely to be normal """

quote6 =    """ Should I kill myself, or have a cup of coffee? """

quote7 =    """ Live to the point of tears """

quote8 =    """ You know what charm is? A way of getting the answer yes
                without having asked any clear questions. """

quote9 =    """ But in the end one needs more courage to live than to kill 
                himself """
                
quote10 =   """ The only way to deal with an unfree world is to become
                so absolutely free that your very existence is an act 
                of rebellion """

quote11 =   """ When I look at my life and its secret colors, 
                I feel like bursting into tears """
                
quote12 =   """ Blessed are the hearts that can bend; they shall never
                be broken """

quote13 =   """ Real generosity toward the future lies in giving all to 
                the present """

quote14 =   """ Autumn is a second spring when every leaf is a flower """

quote15 =   """ I may not have been sure about what really did interest
                me, but I was absolutely sure about what didn't """

quote16 =   """ Fiction is the lie through which we tell the truth """

quote17 =   """ To be happy, we must not be too concerned with others """

quote18 =   """ I opened myself to the gentle indifference of the world """

quote19 =   """ I used to advertise my loyalty and I don't believe there is
                a single person I loved that I didn't eventually betray """

quote20 =   """ Always go too far, because that's where you'll find the truth"""

quote21 =   """ Do not wait for the last judgement. It comes every day """

quote22 =   """ People hasten to judge in order not to be judged themselves """

quote23 =   """ One must imagine Sisyphus happy """

quote24 =   """ I have no idea what's awaiting me, or what will happen
                when this all ends. For the moment I know this: 
                there are sick people and they need curing """
                
quote25 =   """ There is not love of life without despair about life """

quote26 =   """ I had only a little time left and I didn't want to waste
                it on God. """

quote27 =   """ Seeking what is true is not seeking what is desirable """

quote28 =   """ Since we're all going to die, it's obvious that when and how
                don't matter """
                
quote29 =   """ It is the job of thinking people not to be on the side of the
                executioners """

quote30 =   """ When you have once seen the flow of happiness on the 
                face of a beloved person, you know that a man can have
                no vocation but to awaken that light on the faces
                surrounding him """
                
quote31 =   """ Every act of rebellion expresses a nostalgia
                for innocence and an appeal to the essence of being """

quote32 =   """ Life can be magnificent and overwhelming. That is the whole
                tragedy. Without beauty, love, or danger, it would almost be
                easy to live """

quote33 =   """ What is a rebel? A man who says no """

quote34 =   """ Freedom is nothing but a chance to be better """

quote35 =   """ There is scarcely any passion without struggle """

quote36 =   """ Men are never convinced of your reasons, of your sincerity,
                of the seriousness of your sufferings,
                except by your death. So long as you are alive,
                your case is doubtful. You have a right only
                to their skepticism. """
                
quote37 =   """ I leave Sisyphus at the foot of the mountain. One always
                finds one's burden again. But Sisphyus teaches the higher
                fidelity that negates the gods and raises rocks. 
                He too concludes that all is well. This universe
                henceforth without a master seems to him neither sterile
                nor futile. Each atom of that stone, each mineral flake
                of that night-filled mountain, in itself, forms a world.
                The struggle itself toward the heights is enough to fill
                a man's heart. One must imagine Sisyphus happy """
                
quote38 =   """ I rebel, therefore I exist """

quote39 =   """ What is called a reason for living is also an excellent
                reason for dying """

quote40 =   """ The evil that is in the world almost always comes from
                ignorance, and good intentions may do as much harm as
                malevolence if they lack understanding """

quote41 =   """ Where there is no hope, it is incumbent on us to invent it """

quote42 =   """ You can't create experience, you undergo it """

quote43 =   """ Always there comes an hour when one is weary of one's work and 
                devotion to duty, and all one craves for is a loved face,
                the warmth and wonder of a loving heart """

quote44 =   """ I know that man is capable of great deeds. But if he isn't
                capable of great emotion, well, he leaves me cold """

quote45 =   """ Beauty is unbearable, drives us to despair, offering 
                us for a minute the glimpse of an eternity that we
                should like to stretch out over the whole time """
                
quote46 =   """ The most important thing you do everyday you live is 
                deciding not to kill yourself """
                
quote47 =   """ Peace is the only battle worth waging """

quote48 =   """ Have you no hope at all? And do you really live with the thought
                that when you die, you die, and nothing remains? Yes, I said """
                
quote49 =   """ The absurd is the essential concept and the first truth """
          
quoteArray =   [quote1,quote2,quote3,quote4,quote5,quote6,quote7,quote8,
                quote9, quote10, quote11, quote12, quote13, quote14,
                quote15, quote16, quote17, quote18, quote19, quote20, quote21,
                quote23, quote23, quote24, quote25, quote26, quote27, quote28,
                quote29, quote30, quote31, quote32, quote33, quote34, quote35,
                quote36, quote37, quote38, quote39, quote40, quote41, quote42,
                quote43, quote44, quote45, quote46, quote47, quote48, quote49]


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "Camus Quotes - " + title,
            'content': "Camus Quotes generated this quote - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Quote Generated"
    randomInt = random.randint(0,len(quoteArray)-1)

    speech_output = quoteArray[randomInt]
                        
    # Read more at http://www.marieclaire.co.uk/entertainment/people/donald-trump-quotes-57213#LxHIpvwB91ZGyRCx.99"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Here is a Camus quote"
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "CamusQuote":
        return get_welcome_response()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
