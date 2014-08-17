import sys
import json

from collections import defaultdict



STATE_BOUNDING_BOXES = {
    'AL': [-88.4711, 30.2198, -84.8892, 35.0012],
    'AK': [172.4613, 51.2184, -129.9863, 71.3516],
    'AZ': [-114.8152, 31.3316, -109.0425, 37.0003],
    'AR': [-94.6162, 33.0021, -89.6432, 36.5019],
    'CA': [-124.4108, 32.5366, -114.1361, 42.0062],
    'CO': [-109.0480, 36.9948, -102.0430, 41.0039],
    'CT': [-73.7272, 40.9875, -71.7993, 42.0500],
    'DE': [-75.7865, 38.4517, -75.0471, 39.8318],
    'DC': [-77.1174, 38.7912, -76.9093, 38.9939],
    'FL': [-87.6331, 24.5457, -80.0312, 31.0030],
    'GA': [-85.6067, 30.3567, -80.8417, 35.0012],
    'HI': [-160.2300, 18.9209, -154.8078, 22.2290],
    'ID': [-117.2415, 41.9952, -111.0471, 49.0002],
    'IL': [-91.5108, 36.9729, -87.4962, 42.5101],
    'IN': [-88.0603, 37.7725, -84.7851, 41.7597],
    'IA': [-96.6372, 40.3795, -90.1635, 43.5014],
    'KS': [-102.0539, 36.9948, -94.5943, 40.0016],
    'KY': [-89.5720, 36.4964, -81.9700, 39.1472],
    'LA': [-94.0412, 28.9273, -88.8162, 33.0185],
    'ME': [-71.0818, 43.0578, -66.9522, 47.4612],
    'MD': [-79.4889, 37.9149, -75.0471, 39.7223],
    'MA': [-73.5081, 41.2449, -69.9262, 42.8880],
    'MI': [-90.4154, 41.6940, -82.4136, 48.1897],
    'MN': [-97.2287, 43.5014, -89.4898, 49.3836],
    'MS': [-91.6532, 30.1760, -88.0987, 34.9957],
    'MO': [-95.7664, 35.9980, -89.1010, 40.6150],
    'MT': [-116.0475, 44.3613, -104.0475, 49.0002],
    'NE': [-104.0530, 40.0016, -95.3063, 43.0030],
    'NV': [-120.0019, 35.0012, -114.0429, 42.0007],
    'NH': [-72.5551, 42.6963, -70.7039, 45.3033],
    'NJ': [-75.5620, 38.9336, -73.8915, 41.3599],
    'NM': [-109.0480, 31.3316, -103.0014, 37.0003],
    'NY': [-79.7628, 40.4946, -71.8541, 45.0185],
    'NC': [-84.3196, 33.8455, -75.4579, 36.5895],
    'ND': [-104.0475, 45.9332, -96.5606, 49.0002],
    'OH': [-84.8180, 38.4243, -80.5186, 41.9788],
    'OK': [-103.0014, 33.6374, -94.4300, 37.0003],
    'OR': [-124.5532, 41.9952, -116.4638, 46.2672],
    'PA': [-80.5186, 39.7223, -74.6966, 42.2691],
    'RI': [-71.8596, 41.1518, -71.1202, 42.0171],
    'SC': [-83.3392, 32.0327, -78.5414, 35.2148],
    'SD': [-104.0585, 42.4882, -96.4346, 45.9441],
    'TN': [-90.3114, 34.9847, -81.6468, 36.6771],
    'TX': [-106.6381, 25.8383, -93.5154, 36.5019],
    'UT': [-114.0484, 37.0003, -109.0425, 42.0007],
    'VT': [-73.4369, 42.7291, -71.4652, 45.0130],
    'VA': [-83.6733, 36.5512, -75.2443, 39.4649],
    'WA': [-124.7339, 45.5443, -116.9183, 49.0002],
    'WV': [-82.6437, 37.2029, -77.7199, 40.6370],
    'WI': [-92.8855, 42.4936, -86.8061, 47.0778],
    'WY': [-111.0525, 40.9984, -104.0530, 45.0021],
    'PR': [-67.9381, 17.9296, -65.2598, 18.5156]
}



def find_state(coordinates):
    for state, values in STATE_BOUNDING_BOXES.iteritems():
        if values[0] < coordinates[0][0] and values[2] > coordinates[2][0] and values[1] < coordinates[0][1] and values[3] > coordinates[2][1]:
            return state
    return None



def load_scores(filepath):
    scores = {}

    with open(filepath) as file:
        for line in file:
            term, score  = line.split("\t")
            scores[term] = int(score)

    return scores



def sentiment_by_state(lines, scores):
    states_score = defaultdict(int)

    for data in lines:
        if 'text' in data and 'place' in data:
            place = data['place']
            if place and 'bounding_box' in place:
                bounding_box = place['bounding_box']
                if bounding_box and 'coordinates' in bounding_box:
                    coordinates = bounding_box['coordinates']

                    state = find_state(coordinates[0])
                    if state:
                        sentiment = 0
                        words = data['text'].split(' ')
                        for word in words:
                            word = word.lower()
                            if word in scores:
                                sentiment += scores[word]
                        states_score[state] += sentiment

    return states_score



def main(argv):
    lines = []

    with open(argv[1]) as file:
        for line in file:
            lines.append(json.loads(line))


    scores       = load_scores(argv[0])
    sentiments   = sentiment_by_state(lines, scores)

    score_states = {score: state for state, score in sentiments.iteritems()}

    print 
    print 'state with greatest sentiment: ', score_states[max(score_states.keys())]
    print 



if __name__ == '__main__':
    main(sys.argv[1:])
