import numpy as np
import pandas as pd
import os

basic_funcs = ['len(', 'print(', 'display(', 'range(', 'enumerate(', 'zip(', 'int(',
				 'float(', 'complex(', 'bool(', 'tuple(', 'type(', 'readline(']
lists_funcs = ['list(', '.append(', '.extend(', '.insert(', '.remove(', 'del', 
				'.pop(', '.reverse(', '.copy(', '.join(', '.sort(']
strng_funcs = ['str(', '.lstrip(', '.rstrip(', '.upper(', '.lower(', '.count(', 
				'.replace(', '.split(','.format(']
numpy_funcs = ['np.array(', '.dtype', '.astype(', 'np.append(', 'np.insert(', 
				'np.flip(', 'np.tolist(', '.sum(', '.mean(', '.median(', 
				'.max(', '.min(', 'np.std(', 'np.pi', 'np.e', 'np.inf', 'np.nan', 
				'np.absolute(', 'np.round(', 'np.sqrt(', 'np.exp(', 'np.sin(', 'np.cos(', 
				'np.zeros(', 'np.ones(', 'np.full(', 'np.arange(', 'np.linspace(', '.size', 
				'.ndim', '.shape', '.reshape(', ',flatten(', '.transpose(', '.vstack(', 
				'.hstack(', 'np.genfromtxt(','np.meshgrid(']
dates_funcs = ['datetime.now()', '.year', '.month', '.day', '.hour', '.minute', '.second', 
				'.microsecond', 'datetime.strptime', 'datetime.strftime', '.total_seconds()', 
				'timedelta', 'mdates.date2num(']
panda_funcs = ['.Series(', '.index', '.values', '.loc[', '.iloc[', 'pd.concat(', 'pd.DataFrame(', 
				'.describe(', '.to_csv(', '.read_csv(', '.read_excel(']
xrray_funcs = ['.open_dataset(','.open_mfdataset(', '.attrs', '.isel(', '.sel(', '.item']
scipy_funcs = ['stats.linregress(', 'interpolate.interp1d(', 'interpolate.griddata(']
plots_funcs = ['.figure(', '.subplots(', '.xlabel(', '.ylabel(', '.set_xlabel(', 
				'.set_ylabel(', '.grid', '.colorbar', '.set_label', '.clabel', 
				'.invert_yaxis', '.gca', '.axes', '.coastlines', '.add_feature(', 
				'.set_extent(']
plots_types = ['.plot(', '.scatter(', '.hist(', '.contour(', '.contourf(', '.pcolormesh(']
logic_funcs = [' if ', ' while ', ' for ', ' is ', ' in ', ' not ', ' else:', ' elif ', ' and ', '~', '==', '!=', '>=', '<=']

all_funcs = basic_funcs + lists_funcs + strng_funcs + numpy_funcs + dates_funcs + panda_funcs + xrray_funcs + scipy_funcs + plots_funcs + plots_types + logic_funcs

# Metrics to calculate: percent of total commands used, different plotting types, 
#   unique import statements (and possibly number of repeats)

fdir = '/Users/kchristensen/Desktop/Final_project_code/'
filenames = os.listdir(fdir)

figc = []; subc = []
snames = []; percs = []
plts = []; impc = []
logs = []
for fname in filenames:
	f = open(fdir+fname,'r')
	allstr = ''
	for lines in f:
		if not lines.startswith('#'):
			allstr += lines.replace('\n',' ')
	f.close()
	func_count = np.zeros(len(all_funcs))
	for ind, func in enumerate(all_funcs):
		func_count[ind] = allstr.count(func)
	plt_count = np.zeros(len(plots_types))
	for ind, pltf in enumerate(plots_types):
		plt_count[ind] = allstr.count(pltf)
	log_count = np.zeros(len(logic_funcs))
	for ind, pltf in enumerate(logic_funcs):
		log_count[ind] = allstr.count(pltf)

	impc += [allstr.count('import numpy')]
	figc += [allstr.count('.figure(')]
	subc += [allstr.count('.subplots(')]
	snames += [fname.split('.')[0]]
	percs += [sum(func_count>0)/len(all_funcs) * 100]
	plts += [list(plt_count)]
	logs += [list(log_count)]

plts = np.array(plts)
logs = np.array(logs)

func_data = pd.DataFrame(data=snames,columns=['Name'])
func_data['Percent of Total'] = percs
func_data['Figure Count'] = figc
func_data['Subplot Count'] = subc
func_data['Repeat Import'] = impc
for ind, pltf in enumerate(plots_types):
	func_data[pltf] = plts[:,ind]
for ind, logf in enumerate(logic_funcs):
	func_data[logf] = logs[:,ind]

func_data.to_csv(path_or_buf = fdir[0:-19] + 'Final_Project_Data.csv')
