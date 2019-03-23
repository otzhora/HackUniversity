import librosa

def get_bmp(file_path, bpm_guess=120):
    # on most tracks works fine w\ guess 120

    y, sr = librosa.load(file_path, sr=44000)
    hop_length = 512
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr, hop_length=hop_length, start_bpm=bpm_guess)

    return tempo, beats

if __name__ == '__main__':
    path = '/Users/yra/Desktop/study/hack_university/server/static/music/Queen_-_Dont_Stop_Me_Now.mp3'

    guess = 40
    tempo, beats = get_bmp(path, bpm_guess=guess)
    print('Estimated tempo: {:0.2f} beats per minute with guess: {}'.format(tempo, guess))

    guess = 60
    tempo, beats = get_bmp(path, bpm_guess=guess)
    print('Estimated tempo: {:0.2f} beats per minute with guess: {}'.format(tempo, guess))

    guess = 70
    tempo, beats = get_bmp(path, bpm_guess=guess)
    print('Estimated tempo: {:0.2f} beats per minute with guess: {}'.format(tempo, guess))

    guess = 80
    tempo, beats = get_bmp(path, bpm_guess=guess)
    print('Estimated tempo: {:0.2f} beats per minute with guess: {}'.format(tempo, guess))

    guess = 100
    tempo, beats = get_bmp(path, bpm_guess=guess)
    print('Estimated tempo: {:0.2f} beats per minute with guess: {}'.format(tempo, guess))

    guess = 120
    tempo, beats = get_bmp(path, bpm_guess=guess)
    print('Estimated tempo: {:0.2f} beats per minute with guess: {}'.format(tempo, guess))

    guess = 140
    tempo, beats = get_bmp(path, bpm_guess=guess)
    print('Estimated tempo: {:0.2f} beats per minute with guess: {}'.format(tempo, guess))

    