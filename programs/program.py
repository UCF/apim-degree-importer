class Program:
    name = ''
    college = ''
    department = ''
    level = ''
    career = ''
    degree = ''
    online = False
    thesis = False

    def __init__(self, data):
        self.name = data['PlanName']
        self.college = data['College_Full']
        self.department = data['Dept_Full']
        self.career = data['Career']
        self.level = data['Level']
        self.degree = data['Meta Data'][0]['Degree']
        self.online = data['Meta Data'][0]['UCFOnline']
        self.thesis = data['Meta Data'][0]['TotThesis']
