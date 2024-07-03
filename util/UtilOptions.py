import os

class UtilOptions:
  scope = "playlist-modify-private playlist-read-private user-library-read user-read-playback-position"
  redirectUri = "http://localhost:8080"
  excludePlaylists = []
  musicDir = "output/downloader/"
  onlyMyPlaylists = False
  spotifyClientId=""
  spotifyClientSecret=""
  moviesDir=""
  compilerData="./dataFiles/compilerData.txt"
  podcastPlaylist=''
  podcasts=[]
  daysToWaitBeforeRemoving=-1
  
  def __init__(self, dataFile=""):
    if dataFile == "":
      return
    
    if not os.path.exists(dataFile):
      dataFile = os.path.join('../', dataFile)
    
    with open(dataFile, 'r') as f:
      for l in f.readlines():
        key, val = self.parseLine(l)
        
        if key == "" or val == "":
          continue
        
        match key:
          case 'musicDir':
            self.musicDir = val
          case "onlyMyPlaylists":
            b = val.upper()[0]
            self.onlyMyPlaylists = b == 'T' or b == '1'
          case "excludePlaylists":
            self.excludePlaylists = val
          case "spotifyClientId":
            self.spotifyClientId = val
          case "spotifyClientSecret":
            self.spotifyClientSecret = val
          case "moviesDir":
            self.moviesDir = val
          case 'compilerData':
            self.compilerData = val
          case 'podcasts':
            self.podcasts = val
          case 'podcastPlaylist':
            self.podcastPlaylist = val
          case 'daysToWaitBeforeRemoving':
            self.daysToWaitBeforeRemoving = int(val)
  
  def parseLine(self, l):
    i = 0
    quote = False
    list = False
    key = ""
    val = ""
    tmp = ""
  
    while True:
      c = l[i]
      i += 1
    
      if c == '#' and not quote:
        break
      if c == '\'' or c == '"':
        quote = not quote
        continue
      if c == '[' and not quote:
        list = True
        continue
      if c == ']' and not quote and list:
        val = self.parseList(tmp)
        return key, val
      if c == '=':
        key = tmp
        tmp = ""
        continue
      if c == '\n':
        break
    
      tmp += c
    
      if i >= len(l):
        break
        
    val = tmp
    return key, val
  
  def parseList(self, valStr):
    valsList = []
    val = ""
    i = 0
    quote = False
    
    while i < len(valStr):
      char = valStr[i]
      
      if char == '\"' or char == '\'':
        quote = not quote
        continue
      
      if char == ',' and not quote:
        valsList.append(val.strip(' '))
        val = ""
        i += 1
        continue
      
      if char == '\\':
        i += 1
        char = valStr[i]
      
      val += char
      i += 1
    
    return valsList
