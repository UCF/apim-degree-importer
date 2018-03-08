from programs.subplan import Subplan

class Program:
    name = ''
    college = ''
    department = ''
    level = ''
    career = ''
    degree = ''
    online = False
    thesis = False

    @property
    def has_online(self):
        return any(x for x in self.subplans if x.online == True)

    @property
    def online_subplan(self):
        return next((x for x in self.subplans if x.online == True), None)

    @property
    def has_subplans(self):
        if len( self.subplans > 0 ):
            return True
        return False

    def __init__(self, data):
        self.name = data['PlanName']
        self.college = data['College_Full']
        self.department = data['Dept_Full']
        self.career = data['Career']
        self.level = data['Level']
        self.degree = data['Meta Data'][0]['Degree']
        self.online = data['Meta Data'][0]['UCFOnline']
        self.thesis = data['Meta Data'][0]['TotThesis']
        self.subplans = []

        _subplans = data['SubPlans']

        for sp in data['SubPlans']:
            subplan = Subplan(sp)
            self.subplans.append(subplan)
