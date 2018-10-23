from pylsl import StreamInlet, resolve_stream
import pandas as pd

streams = resolve_stream('type', 'NIRS')
inlet = StreamInlet(streams[0])

data = []
while True:
    sample, timestamp = inlet.pull_sample()
    data.append(sample)
    print(len(data), timestamp, sample)
    if len(data) > 30:
        break

df = pd.DataFrame(data)
df.to_excel("aaa.xlsx")
