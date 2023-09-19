#%%
def add_names_to_agg_list(names, aggregate_list = []):
    for name in names:
        aggregate_list.append(name)
    return aggregate_list

# def add_names_to_agg_list(names, aggregate_list = None):
#     if aggregate_list is None:
#         aggregate_list = []
#     for name in names:
#         aggregate_list.append(name)
#     return aggregate_list

print(add_names_to_agg_list(['Samer','Joey','Anne']))
print(add_names_to_agg_list(['Samer','Joey','Anne']))