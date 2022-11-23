elif 'play' or 'video' in text2:
    speak('You want to play which video?')
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 3.2)
        print('listening...')
        audio = r.listen(source)
        video = r.recognize_google(audio)
    speak('Playing {} on youtube'.format(video))
    print('Playing {} on youtube'.format(video)) 

    assist = music()
    assist.play(video)    