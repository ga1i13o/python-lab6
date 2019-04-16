import requests

base_uri = 'http://localhost:5000/api/v1'

if __name__=='__main__':
    #requests.post(base_uri+'/tasks', json={'todo': "Go home", 'urgency': "true"})

    requests.put(base_uri+'/tasks/15', json={'urgency': "true"})
    requests.put(base_uri + '/tasks/15', json={'todo': "Get out of this house"})
    tasks = requests.get(base_uri+'/tasks')
    tasklist = tasks.json()

    for t in tasklist:
        print("{ id:" + str(t['id']) + ", todo: " + t['todo'] + ", urgency: " + t['urgency']+ " }")