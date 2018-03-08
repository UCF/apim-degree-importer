class Subplan:
    """
    Object for describing a subplan
    """
    sp_code = ''
    name = ''
    plan_type = ''
    degree = ''
    thesis = ''
    online = False

    def __init__(self, sp):
        self.code = sp['Subplan']
        self.name = sp['Subplan_Name']
        self.plan_type = sp['Meta Data'][0]['Plan Type']
        self.degree = sp['Meta Data'][0]['Degree']
        self.thesis = sp['Meta Data'][0]['TotThesis']
        self.online = False

        if sp['Meta Data'][0]['UCFOnline'] == "1":
            self.online = True
