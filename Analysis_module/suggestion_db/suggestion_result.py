import random


def suggest_joy():
    joy_list =[]
    joy_prompt_list = ["Have a lovely day.",
                       "Keep it up! You are looking great.",
                       "Isn't life beautiful ?!",
                       "Somebody looks happy :)"]
    joy_quote_list = ["Keep up the good mood! A nice morning walk will keep your spirits high for rest of the day.",
                "Spread the love. Be happy, be nice to everyone. This is the most important thing to cherish your close ones.",
                "Nice! Hard work always pays off. Keep working hard!",
                "If work-life balance is maintained then you always will be happy",
                "Settle down, have a nice relaxing bath. You will feel even more amazing",
                "Cherish these moments. They are some of the most life defining moments of your life",
                "Work hard and party harder!",
                "There is only one happiness in this life, to love and be loved."]

    joy_video_list = ["Enjoy yourselves: https://www.youtube.com/watch?v=ZbZSe6N_BXs",
                      "True joy of life is being happy: https://www.youtube.com/watch?v=MDPkgWGDYkM",
                      "Knowledge is the true happiness: https://www.youtube.com/watch?v=kfDvdYj0_fA",
                      "Happiness is appreciating little things in life: https://www.youtube.com/watch?v=v6Agqm4K7Ok",
                      "Life is one amazing thing: https://www.youtube.com/watch?v=eIdJ22AfsO8",
                      "Keep smiling: https://www.youtube.com/watch?v=C4Uc-cztsJo",
                      "Appreciate the beauty everywhere: https://www.youtube.com/watch?v=Dceyy0cX6J4",
                      "Truly beautiful: https://www.youtube.com/watch?v=8S0FDjFBj8o"]

    return random.choice(joy_prompt_list),random.choice(joy_quote_list),random.choice(joy_video_list)

def suggest_confident():
    confident_prompt_list = ["Great to see such confident attitude.",
                       "You are one amazing person with such high self esteem.",
                       "Strong confidence and great personality is the way to awesome life!",
                       "Your personality is glowing with confidence!"]

    confident_quote_list = ["Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence.",
                "Beauty has so many forms, and I think the most beautiful thing is confidence and loving yourself. ",
                "Positivity, confidence, and persistence are key in life, so never give up on yourself. ",
                "As long as you keep going, you'll keep getting better. And as you get better, you gain more confidence. That alone is success.",
                "Settle down, have a nice relaxing bath. You will feel even more amazing",
                "The most beautiful thing you can wear is confidence.",
                "All you need in this life is hard work and confidence, and then success is sure.",
                "When you have confidence, you can have a lot of fun. And when you have fun, you can do amazing things."]

    confident_video_list = ["Enjoy yourselves: https://www.youtube.com/watch?v=ZbZSe6N_BXs",
                      "True joy of life is being happy: https://www.youtube.com/watch?v=MDPkgWGDYkM",
                      "Knowledge is the true happiness: https://www.youtube.com/watch?v=kfDvdYj0_fA",
                      "Happiness is appreciating little things in life: https://www.youtube.com/watch?v=v6Agqm4K7Ok",
                      "Life is one amazing thing: https://www.youtube.com/watch?v=eIdJ22AfsO8",
                      "Keep smiling: https://www.youtube.com/watch?v=C4Uc-cztsJo",
                      "Appreciate the beauty everywhere: https://www.youtube.com/watch?v=Dceyy0cX6J4",
                      "Truly beautiful: https://www.youtube.com/watch?v=8S0FDjFBj8o"]

    return (random.choice(confident_prompt_list),random.choice(confident_quote_list),random.choice(confident_video_list))

def suggest_Analytical():

    Analytical_prompt_list = ["Systematic person is considered an ideal person.",
                       "Analytical person is always precise!",
                       "Just sit back and relax for some time, you have earned it.",
                       "Analytical mindset is hard to find."]
    Analytical_quote_list = ["The approach preferred to solve tough the problems is the analytical one.",
                "Logical reasoning makes man a rational, strong and a smart person.",
                "Nice! Hard work always pays off. Keep working hard!",
                "If work-life balance is maintained then you always will be happy",
                "A rational and logical man is always a wise man.",
                "You have to really dive deep back into yourself and keep the mind strong to stay analytical.",
                "Modern definition of methodical person is the person who is capable of doing anything."]

    Analytical_video_list = ["Enjoy yourselves: https://www.youtube.com/watch?v=ZbZSe6N_BXs",
                      "True joy of life is being happy: https://www.youtube.com/watch?v=MDPkgWGDYkM",
                      "Knowledge is the true happiness: https://www.youtube.com/watch?v=kfDvdYj0_fA",
                      "Happiness is appreciating little things in life: https://www.youtube.com/watch?v=v6Agqm4K7Ok",
                      "Life is one amazing thing: https://www.youtube.com/watch?v=eIdJ22AfsO8",
                      "Keep smiling: https://www.youtube.com/watch?v=C4Uc-cztsJo",
                      "Appreciate the beauty everywhere: https://www.youtube.com/watch?v=Dceyy0cX6J4",
                      "Truly beautiful: https://www.youtube.com/watch?v=8S0FDjFBj8o"]


    return (random.choice(Analytical_prompt_list),random.choice(Analytical_quote_list),random.choice(Analytical_video_list))


def suggest_neutral():
    neutral_prompt_list = ["Hey, looks like you are having an unadventurous day",
                           "Every day should be an adventure",
                           "Day with mixed emotions is a step towards a happy day."]
    neutral_quote_list = ["Biggest risk you can take in your life is not taking any risk",
                    "Hey, Rubik's cube in trend these days. Can you solve one ?",
                    "That man has reached immortality who is disturbed by nothing material.",
                    "Good, better, best. Never let it rest. 'Til your good is better and your better is best.",
                    "With the new day comes new strength and new thoughts.",
                    "Life is 10% what happens to you and 90% how you react to it."]
    neutral_video_list = ["Never stop believing: https://www.youtube.com/watch?v=1k8craCGpgs",
                 "Enjoy this amazing melody: https://www.youtube.com/watch?v=IbwqdS9Y1OY",
                 "Have a look at this month's most popular video song:https://www.youtube.com/watch?v=8_03FqAr2f8",
                 "Risk Everything: https://www.youtube.com/watch?v=pCVF0CSRTYA",
                 "You should never give up: https://www.youtube.com/watch?v=uMJ5Zwfz1pU",
                 "Create a better tomorrow: https://www.youtube.com/watch?v=uMJ5Zwfz1pU"]

    return random.choice(neutral_prompt_list),random.choice(neutral_quote_list),random.choice(neutral_video_list)


def suggest_sad():
    sad_prompt_list = ["Sad days are just a part of life.",
                       "Not having a good day huh?!",
                       "Sadness is just a state of mind.",]
    sad_quote_list = ["Arise! Awake! and stop not until the goal is reached.",
                "The world is the great gymnasium where we come to make ourselves strong.",
                "Never think there is anything impossible for the soul. It is the greatest heresy to think so. If there is sin, this is the only sin; to say that you are weak, or others are weak.",
                "Some days are just bad days, that's all. You have to experience sadness to know happiness, and I remind myself that not every day is going to be a good day, that's just the way it is! ",
                "The word 'happy' would lose its meaning if it were not balanced by sadness.",
                "I do believe that if you haven't learnt about sadness, you cannot appreciate happiness.",
                "Affliction comes to us, not to make us sad but sober; not to make us sorry but wise.",
                "Sadness is but a wall between two gardens."]

    sad_video_list = ["This will cheer you up: https://www.youtube.com/watch?v=nIp5Tfkgwf4",
                 "Never stop believing: https://www.youtube.com/watch?v=1k8craCGpgs",
                 "Enjoy this amazing melody: https://www.youtube.com/watch?v=IbwqdS9Y1OY",
                 "Have a look at this month's most popular video song:https://www.youtube.com/watch?v=8_03FqAr2f8",
                 "Risk Everything: https://www.youtube.com/watch?v=pCVF0CSRTYA",
                 "You should never give up: https://www.youtube.com/watch?v=uMJ5Zwfz1pU",
                 "Create a better tomorrow: https://www.youtube.com/watch?v=uMJ5Zwfz1pU",
                "Keep moving forward: https://www.youtube.com/watch?v=AjZ0KbJcav0",
                "Leaders are created through the mould of hard work: https://www.youtube.com/watch?v=fPeDDeHraA8",
                "Never lose hope: https://www.youtube.com/watch?v=VFX2Nqwwm44",
                "Window of opportunity is always open: https://www.youtube.com/watch?v=1GHS6Wmk5tg",
                "Just sit back and relax for some time: https://www.youtube.com/watch?v=-hIc_epqfI0",
                "https://www.youtube.com/watch?v=7dDvZ2qZYe8",
                "https://www.youtube.com/watch?v=uG6vdt0olSA"]

    return random.choice(sad_prompt_list),random.choice(sad_quote_list),random.choice(sad_video_list)

def suggest_fear():
    fear_prompt_list = ["Confidence is the key to success.",
                       "Fear not, I'm here.",
                       "Fear is just a state of mind.",]

    fear_quote_list = [ "Victory is eminent if you can overcome fear.",
                "The world is the great gymnasium where we come to make ourselves strong.",
                "Never think there is anything impossible for the soul. It is the greatest heresy to think so. If there is sin, this is the only sin; to say that you are weak, or others are weak.",
                "Some days are just bad days, that's all. You have to experience sadness to know happiness, and I remind myself that not every day is going to be a good day, that's just the way it is! ",
                "Fear weakens our thought process by a large margin",
                "THe precess of overcoming fear is a necessary step if you want to live happily.",
                "Affliction comes to us, not to make us sad but sober; not to make us sorry but wise.",
                "Fear is but a wall between awesomeness."]

    fear_video_list = ["This will cheer you up: https://www.youtube.com/watch?v=nIp5Tfkgwf4",
                 "Never stop believing: https://www.youtube.com/watch?v=1k8craCGpgs",
                 "Enjoy this amazing melody: https://www.youtube.com/watch?v=IbwqdS9Y1OY",
                 "Have a look at this month's most popular video song:https://www.youtube.com/watch?v=8_03FqAr2f8",
                 "Risk Everything: https://www.youtube.com/watch?v=pCVF0CSRTYA",
                 "You should never give up: https://www.youtube.com/watch?v=uMJ5Zwfz1pU",
                 "Create a better tomorrow: https://www.youtube.com/watch?v=uMJ5Zwfz1pU",
                "Keep moving forward: https://www.youtube.com/watch?v=AjZ0KbJcav0",
                "Leaders are created through the mould of hard work: https://www.youtube.com/watch?v=fPeDDeHraA8",
                "Never lose hope: https://www.youtube.com/watch?v=VFX2Nqwwm44",
                "Window of opportunity is always open: https://www.youtube.com/watch?v=1GHS6Wmk5tg",
                "Just sit back and relax for some time: https://www.youtube.com/watch?v=-hIc_epqfI0",
                "https://www.youtube.com/watch?v=7dDvZ2qZYe8",
                "https://www.youtube.com/watch?v=uG6vdt0olSA"]

    return random.choice(fear_prompt_list),random.choice(fear_quote_list),random.choice(fear_video_list)

def suggest_anger():
    anger_prompt_list = ["Dont be angry, be peaceful!",
                       "Anger makes a man vulnerable.",
                       "An angry man is never a wise man.",]

    anger_quote_list = [ "Keep calm and think rationally!",
                "The world is the great gymnasium where we come to make ourselves strong.",
                "Post prominent ritual of finding ourselves involves controlling our anger",
                "Why take so much stess when you can ignore the unimportant things.",
                "The word 'happy' would lose its meaning if it were not tackled by Anger.",
                "Anger management is very hard. That is why only few can manage it.",
                "Affliction comes to us, not to make us sad but sober; not to make us sorry but wise.",
                "Anger prevents us from taking wise decisions."]

    anger_video_list = ["This will cheer you up: https://www.youtube.com/watch?v=nIp5Tfkgwf4",
                 "Never stop believing: https://www.youtube.com/watch?v=1k8craCGpgs",
                 "Enjoy this amazing melody: https://www.youtube.com/watch?v=IbwqdS9Y1OY",
                 "Have a look at this month's most popular video song:https://www.youtube.com/watch?v=8_03FqAr2f8",
                 "Risk Everything: https://www.youtube.com/watch?v=pCVF0CSRTYA",
                 "You should never give up: https://www.youtube.com/watch?v=uMJ5Zwfz1pU",
                 "Create a better tomorrow: https://www.youtube.com/watch?v=uMJ5Zwfz1pU",
                "Keep moving forward: https://www.youtube.com/watch?v=AjZ0KbJcav0",
                "Leaders are created through the mould of hard work: https://www.youtube.com/watch?v=fPeDDeHraA8",
                "Never lose hope: https://www.youtube.com/watch?v=VFX2Nqwwm44",
                "Window of opportunity is always open: https://www.youtube.com/watch?v=1GHS6Wmk5tg",
                "Just sit back and relax for some time: https://www.youtube.com/watch?v=-hIc_epqfI0",
                "https://www.youtube.com/watch?v=7dDvZ2qZYe8",
                "https://www.youtube.com/watch?v=uG6vdt0olSA"]

    return random.choice(anger_prompt_list),random.choice(anger_quote_list),random.choice(anger_video_list)

def give_suggestion(prominent_emotion):

    res = ''
    if (prominent_emotion == 'Joy'):
        res = suggest_joy()
    elif (prominent_emotion == 'Confident'):
        res = suggest_confident()
    elif (prominent_emotion == 'Analytical'):
        res = suggest_Analytical()
    elif (prominent_emotion == 'Tentative'):
        res = suggest_neutral()
    elif (prominent_emotion == 'Sadness' ):
        res = suggest_sad()
    elif (prominent_emotion == 'Fear' ):
        res = suggest_fear()
    elif (prominent_emotion == 'Anger' ):
        res = suggest_anger()
    else:
        return ("Not a good day huh?!","Trick is to get yourself into the zone and live like it is the last day of your life","Never stop believing: https://www.youtube.com/watch?v=1k8craCGpgs")
    return (res)

