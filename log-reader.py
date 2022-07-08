file = 'qgames.log'


def open_file(file: str) -> list:
  data=[]
  mach_game=[]
  temp_data=[]
  flag=False
  with open(file,'r') as f:
      for line in f:
          if line.startswith('  0:00 InitGame:'):
              flag=True
          # elif 'InitGame' in line:
          #     flag=True
          elif line.strip().endswith('ShutdownGame:'):
              data.append(temp_data)
              temp_data = []
              flag=False
          elif flag:
              temp_data.append(line)
  print(data)
  return data

def struct_log(data:list):
  test='name'

open_file(file=file)

