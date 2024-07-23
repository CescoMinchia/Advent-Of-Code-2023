import os
import copy

import re

class Workflow():
    workflow_dict = None
    

    def __init__(self):
        self.workflow_dict = {}
        # self.parse_workflow(None,None)

    def add_workflow(self,workflow):
        id = re.search("^\w+(?={)",workflow).group(0)
        conditions = re.search("(?<={).+?(?=})",workflow).group(0).split(",")
        self.workflow_dict[id] = conditions

    # def parse_workflow(self,rating):
    #     workflow = "px{a<2006:qkq,m>2090:A,rfg}"
    #     # rating = "{x=787,m=2655,a=1222,s=2876}"
    #     rating_dict = dict(eval(re.sub(r"[a-zA-Z]", r"'\g<0>'", rating).replace("=",":")))

    #     # id = re.search("^\w+(?={)",workflow).group(0)
    #     conditions = re.search("(?<={).+?(?=})",workflow).group(0).split(",")

    #     for c in conditions:
    #         if ":" not in list(c): # conditions
    #             next_step = c
    #             break
    #         else:
    #             cond_as_literal_str,next_workflow = c.split(":")
    #             # in the condition, we replace the letter (x,m, a or s) with "rating_dict['..']"
    #             parsed_condition =\
    #                 re.sub(r"[a-zA-Z]", r"rating_dict['\g<0>']", cond_as_literal_str)
    #             if eval(parsed_condition):
    #                 next_step = next_workflow
    #                 break
        
    #     if next_step == "A":
    #         return sum(rating_dict.values())
    #     if next_step == "R":
    #         return 0

    #     return self.parse_workflow(self.workflow_dict[next_step],rating) 

    def get_value_from_rating(self,rating):
        # rating is a literal and must be converted as dictionary
        rating_dict = dict(eval(re.sub(r"[a-zA-Z]", r"'\g<0>'", rating).replace("=",":")))
        
        starting_id = "in"
        workflow = self.workflow_dict[starting_id]
        while True:
            # rating = "{x=787,m=2655,a=1222,s=2876}"

            # id = re.search("^\w+(?={)",workflow).group(0)

            for c in workflow:
                # conditions = re.search("(?<={).+?(?=})",step).group(0).split(",")
                if ":" not in list(c): # conditions
                    next_step = c
                    break
                else:
                    cond_as_literal_str,next_workflow = c.split(":")
                    # in the condition, we replace the letter (x,m, a or s) with "rating_dict['..']"
                    parsed_condition =\
                        re.sub(r"[a-zA-Z]", r"rating_dict['\g<0>']", cond_as_literal_str)
                    if eval(parsed_condition):
                        next_step = next_workflow
                        break
            
            if next_step == "A":
                return sum(rating_dict.values())
            if next_step == "R":
                return 0

            workflow = self.workflow_dict[next_step]

def extract_input(filename):
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'input',filename)
    with open(path,"r") as f:
        content = f.read()
    
    x = [i for i in content.split('\n') if i != ""]
    workflow_list = [i for i in x if i[0] != "{"]
    rating_list  = [i for i in x if i[0] == "{"]
    return workflow_list, rating_list

# da sistemare il transpose
def print_input(pattern):
    output = '\n'.join([''.join(i) for i in pattern])
    print(output)

