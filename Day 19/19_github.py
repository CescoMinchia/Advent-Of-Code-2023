from src import helper as h

if __name__ == "__main__":
    workflow_list,rating_list = h.extract_input('long.txt')
    work_obj = h.Workflow()
    for w in workflow_list:
        work_obj.add_workflow(w)
    
    tot = 0
    for r in rating_list:
        tot += work_obj.get_value_from_rating(r)

    print(tot)
    print("END")
