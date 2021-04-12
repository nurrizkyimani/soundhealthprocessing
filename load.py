import librosa

def load_data(path):
  signal, sampling_rate = librosa.load(path)
  return signal, sampling_rate

def testing_path(path):
  print(path)

class audioPreprocessing():
  def __init__(self, path):
    self.path = path
  
  def testing_path(self):
    print(self.path)

  def audioToSpecto():
    pass
  


#fun: data loading
#fun: converting audio signal to spectogram