
# gives threshold values decreasing over time

# threshold should reduce with values 90 60 30 10 5

def thres_value(elapsed_time):
  thres_init = 90
  
  if elapsed_time > 0 and elapsed_time < 151:
    thres_init = thres_init
  elif elapsed_time > 150 and elapsed_time < 301:
    thres_init -= 30
  elif elapsed_time > 450 and elapsed_time < 601:
    thres_init -= 60
  elif elapsed_time > 600 and elapsed_time < 751:
    thres_init -= 80
  elif elapsed_time > 750:
    thres_init -= 85

  #print(str(started_at)[11:-10])
  return thres_init






