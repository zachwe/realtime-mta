import requests
import pandas as pd
import gtfs_realtime_pb2

class RealtimeProcessor:
    url = ("http://datamine.mta.info/mta_esi.php?"
            "key=db5d317858ae0e832c85b30aa13aa8d2"
            "&feed_id=1")

    def __init__(self):
        self.stops = self.getStops()
        self.messages= []

    def getStops(self):
        """Do stuff"""
        stops = pd.read_csv('stops.txt')
        return stops

    def getStopName(self, stop_id):
        return self.stops[self.stops['stop_id'] ==  stop_id].values

    def getRealTimeData(self):
        res = requests.get(RealtimeProcessor.url, stream=True)
        raw_data = res.raw.read()
        feed_message = gtfs_realtime_pb2.FeedMessage()
        feed_message.ParseFromString(raw_data)
        self.messages.append(feed_message)

def main():
    """Do stuff"""
    rtp = RealtimeProcessor()
    rtp.getRealTimeData()
    if len(rtp.messages) > 0:
        for entity in rtp.messages[-1].entity:
            print "Entity: "
            print entity.id
            print entity.trip_update
            print entity.vehicle
            print entity.alert

if __name__ == "__main__":
    main()
