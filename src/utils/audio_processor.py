class AudioProcessor:
    @staticmethod
    def preprocess(audio):
        sr, y = audio
        # Convert to mono if stereo
        if y.ndim > 1:
            y = y.mean(axis=1)
        return sr, y
