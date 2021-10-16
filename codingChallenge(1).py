import json
import pickle


def raceDetailsExtractionAustralia(data):
	finallist = []
	for date in data["dates"]:
		for section in date["sections"]:
			if(section["raceType"]=='horse'):
				for meeting in section["meetings"]:
					raceDetail = {}
					raceDetail["meeting_id"]=meeting["id"]
					raceDetail["meeting_name"]=meeting["name"]
					for event in meeting["events"]:
						if(event["regionGroup"]=="Aus/NZ"):
							raceDetail["raceNumber"]=event["raceNumber"]
							raceDetail["race_link"]=event["httpLink"]
							raceDetail["event_id"]=event["id"]
							raceDetail["distance"]=event["distance"]
							raceDetail["start_time"]=event["startTime"]
							finallist.append(raceDetail)
	return finallist
  
if __name__=="__main__": 
    with open('response.json') as f:
      data = json.load(f)
    
    result = raceDetailsExtractionAustralia(data)
    
    #Writing output
    with open('outfile.data', 'wb') as fp:
      pickle.dump(result, fp)
		