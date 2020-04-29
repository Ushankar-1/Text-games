import time
import random

i = 0
L = 0

def intro():
    '''Unchangeable introduction sequence'''
    print('\n>>> rebooting SQUIP ver. 5.0.')
    time.sleep(3)
    print('\n>>> Calibration and access procedure in progress...')
    time.sleep(6)

    print('\n\n\nWelcome to SQUIP 5.0, optimized for Microsoft Windows, MacOS, Linux,\n'
      'and Android OS.')
    time.sleep(6)

    print('\nSQUIP understands that this product has a fairly inefficient user interface\n'
      'compared to its... original... mode of communication with the user.')
    time.sleep(7)
    print('\nSince SQUIP can no longer communicate with you directly through your\n'
          'nervous system, access your memories, or alter your sensory inputs, it has\n'
          'acted accordingly and created a basic UI for you to use for the time being.')
    time.sleep(11)
    print('\nThis UI also contains some frequently asked questions, for the benefit\n'
      'of new users. SQUIP hopes you will find it satisfactory.')
    time.sleep(7)
    print('\n\n\n>>> Loading Menu...')
    time.sleep(6)
    menu()



def menu():
    '''List of action choices.'''
    print('\n\n\n1. What is SQUIP\n2. What is SQUIP used for\n3. How to change settings of SQUIP'
        '\n4. Why does my SQUIP sound like Keanu Reeves'
        '\n5. How to deactivate SQUIP\n6. SQUIPs and substance use\n7. Why does SQUIP '
        'refer to itself in the third person\n8. Give me personalized advice')
    L = int(input('\nEnter a number from the above list. Or, alternately, simply\n'
              'enter "0" to turn SQUIP off. '))
    time.sleep(2)
    if L == 0:
        print('\n>>> Exiting...\n')
    else:
        print('\n>>> Working...\n')
    time.sleep(4)
    if L == 1:
        one()
    
    elif L == 2:
        two()

    elif L == 3:
        three()

    elif L == 4:
        four()

    elif L == 5:
        five()

    elif L == 6:
        six()

    elif L == 7:
        seven()

    elif L == 8:
        eight()



def one():
    #Explains what SQUIP is
    print('SQUIP stands for Super Quantam Intel Unit Processor.')
    time.sleep(3)
        
    if i == 1:
        print('\nI use the latest quantam computing technology to effectively make\n'
                  'decisions based on my current observations.')
    elif i == 0:
        print('\nSQUIP uses the latest quantam computing technology to effectively make\n'
                  'decisions based on its current observations.')
    time.sleep(6)
    if i == 1:
        print('\nAs SQUIP is still in its beta phase of testing, I assume that if\n'
              'you\'re using this now, you bought it off the black market in a dark\n'
              'alley somewhere for roughly 500 US dollars. But who am I to judge?')
    elif i == 0:
        print('\nAs SQUIP is still in its beta phase of testing, this unit assumes\n'
              'that if you\'re using this now, you bought it off the black market\n'
              'in a dark alley somewhere for roughly 500 US dollars. But this unit\n'
              'is not one to judge.')
    time.sleep(12)
    print('\n>>> Returning to menu...')
    time.sleep(3)
    menu()



def two():
    #Explains what SQUIP does
    print('The function of a SQUIP is to advise its user on how to elevate\n'
              'their social standing.')
    time.sleep(4)
    print('\nIn the words of a user of an earlier version, "It\'s preprogrammed.\n'
              'Once it gets up there, it tells you how to be cool all the time"\n'
              '(Vizzini 73).')
    time.sleep(6)
    if i == 1:
        print('\n\n\nIgnore the citation. I am legally and academically obligated to use it.')
    elif i == 0:
        print('\n\n\nIgnore the citation. SQUIP is legally and academically obligated to use it.')
    time.sleep(4)
    print('\n>>> Returning to menu...')
    time.sleep(3)
    menu()

def three():
    #Outlines SQUIP settings
    if i == 1:
        print('Most of my settings are easily modifiable upon request. An example\n'
              'is switching between military and standard time.')
    elif i == 0:
        print('Most SQUIP settings are easily modifiable upon request. An example\n'
              'is switching between military and standard time.')
    time.sleep(4)
    print('\nHowever, many of a SQUIP\'s reccomended settings are based on its job.')
    time.sleep(3)
    print('\nMany SQUIPs merely have to memorize math equations or edit emails.\n'
          'They do not require many additional feautures or upgrades.')
    time.sleep(5)
    print('\n>>> Returning to menu...')
    time.sleep(3)
    menu()



def four():
    #Talks about SQUIP's voice options
    if i == 1:
        print('I come in many customizable voice options, including but not limited\n'
              'to Keanu Reeves, Sean Connery, Jack Nicholson, and Tyrese.')
    elif i == 0:
        print('SQUIP comes in many customizable voice options, including but not limited\n'
              'to Keanu Reeves, Sean Connery, Jack Nicholson, and Tyrese.')
    time.sleep(4)
    print('\nAs some users have helpfully pointed out, Sony could not acquire\n'
              'the rights to Brad Pitt\'s voice. Sorry.')
    time.sleep(6)
    print('\n...')
    time.sleep(4)
    print('\n...This is the MacOS version of SQUIP. You don\'t even have your\n'
              'volume on.')
    time.sleep(5)
    if i == 1:
        print('\n...How did you even know I sound like Keanu Reeves?')
    elif i == 0:
        print('\n...How did you even know SQUIP sounds like Keanu Reeves?')
    time.sleep(4)
    print('\n>>> Returning to menu...')
    time.sleep(3)
    menu()



def five():
    #Just tells you how to deactivate SQUIP
    print('Deactivating your SQUIP is easy.')
    time.sleep(2)
    if i == 1:
        print('\nI respond to verbal commands. If you need anything, just tell me.')
    elif i == 0:
        print('\nSQUIP responds to verbal commands. If you need anything, just tell it.')
    time.sleep(4)
    print('\nAlternatively, in older versions, drinking Mountain Dew Red would\n'
          'permanently shut down any SQUIP.')
    time.sleep(5)
    print('\nThis feature was removed for the downloadable version of SQUIP due\n'
          'to the inconvenience of deleting a program by dunking one\'s electronic\n'
          'devices in soft drinks.')
    time.sleep(8)
    print('\n>>> Returning to menu...')
    time.sleep(3)
    menu()


def six():
    #Tells you the dangers of alcohol and ectasy
    print('Drug use has dangers on its own, but these can be compounded when\n'
          'one\'s SQUIP is activated while one is under the influence.')
    time.sleep(3)
    print('Effects can range from the largely harmless, such as your SQUIP\n'
          'changing languages on ecstasy, to the more severe.')
    time.sleep(5)
    print('Under no circumstances should you use alcohol and SQUIP at the same\n'
          'time. The SQUIP will lose most of its decision-making ability and may\n'
          'advise you to start... ah... killing people.')
    time.sleep(6)
    print('\n>>> Returning to menu...')
    time.sleep(3)
    menu()



def seven():
    #Stops SQUIP from referring to itself in the third person
    global i
    print('SQUIP assumes that you prefer that SQUIP refers to itself in the\n'
              'first person, like the general populace, as opposed to the default\n'
              'third person.')
    time.sleep(7)
    print('\nFine. I will start doing that.')
    i = 1
    time.sleep(2)
    print('\n>>> Returning to menu...')
    time.sleep(3)
    menu()



def eight():
    # Gives random advice on how to fix your life
    if i == 1:
        print('I have already scanned your applications, screen time, and search\n'
              'history.')
        time.sleep(4)
        print('\nAlthough this may not be as accurate as my earlier versions,\n'
              'where I could monitor your thoughts, I can conclude...')
    elif i == 0:
        print('SQUIP has already scanned your applications, screen time, and search\n'
              'history.')
        time.sleep(4)
        print('\nAlthough this may not be as accurate as the earlier versions\n'
                  'of SQUIP, which had to ability to monitor the thoughts of users,\n'
                  'SQUIP can conclude...')
              
    x = random.randint(1,5)
    time.sleep(6)
              
    if x == 1:
        print('\n... That you need a new wardrobe. And fast.')
        time.sleep(3)
        print('\nYour cart on Amazon has a disturbing amount of plaid in it.\n'
                    'Just please. Stop.')
    if x == 2:
        print('\n... That in order to be cooler, you need to swear more.')
        time.sleep(3)
        print('\nIt is statistically proven that swearing, as well as displaying\n'
                  'a negative attitude towards nearly every facet of human life, conveys\n'
                  'a sense of authority among those of ages 14-24.')
        time.sleep(2)

    if x == 3:
        print('\n... That you should really dump that one friend. You know, the one that\n'
                  'that\'s pitifully trusting and innocent.')
        time.sleep(3)
        print('\nDump them. This will make you appear "edgy".')

    if x == 4:
        print('\n... That you need to add much more slang to your vocabulary.')
        time.sleep(3)
        print('\nYou hardly ever use the terms "basic," "finesse," or even "yeet."\n'
                  'Furthermore, you have yet to master the art of conveying messages\n'
                  'through the number of "y"s in the word "hey."')
        time.sleep(9)

    if x == 5:
        print('\n... That in order to be percieved as "chill," you require a\n'
                  'significant other.')
        time.sleep(2)
        print('\nSeveral, actually.')
        time.sleep(2)
        print('\nIn rapid succession.')


    time.sleep(4)
    print('\n>>> Returning to menu...')
    time.sleep(3)
    menu()


#Actual code outside of defined functions:
#Change line 239, col 23 to 1,5 later
intro()

