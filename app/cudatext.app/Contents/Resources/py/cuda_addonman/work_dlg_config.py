from cudatext import *
from . import opt

def do_config_dialog():
    c1 = chr(1)
    id_channel = 3
    id_readme = 4
    id_confirm = 5
    id_proxy = 7
    id_ok = 8
    all_size_x = 520
    all_size_y = 410
    btn_size = 90

    text = '\n'.join([]+
      [c1.join(['type=label', 'pos=6,6,250,0', 'cap=&Default channels:'])]+
      [c1.join(['type=memo', 'pos=6,24,%d,140'%(all_size_x-6), 'val='+'\t'.join(opt.ch_def), 'props=1,0,1'])]+
      [c1.join(['type=label', 'pos=6,146,256,0', 'cap=&User channels:'])]+
      [c1.join(['type=memo', 'pos=%d,%d,%d,%d'%(6, 164, all_size_x-6, all_size_y-120), 'val='+'\t'.join(opt.ch_user)])]+
      [c1.join(['type=check', 'pos=%d,%d,%d,0'%(6, all_size_y-115, all_size_x-btn_size-12), 'cap=Install: suggest &readme after', 'val='+('1' if opt.suggest_readme else '0') ])]+
      [c1.join(['type=check', 'pos=%d,%d,%d,0'%(6, all_size_y-85, all_size_x-btn_size-12), 'cap=Install: show &confirmation and report', 'val='+('1' if opt.install_confirm else '0') ])]+
      [c1.join(['type=label', 'pos=%d,%d,%d,0'%(6, all_size_y-55, all_size_x-btn_size-12), 'cap=&Proxy, e.g. http://proxy.myserver.com:2010' ])]+
      [c1.join(['type=edit', 'pos=%d,%d,%d,0'%(6, all_size_y-35, all_size_x-6), 'val='+opt.proxy ])]+
      [c1.join(['type=button', 'pos=%d,%d,%d,0'%(all_size_x-2*btn_size-12, all_size_y-0, all_size_x-btn_size-12), 'cap=&OK'])]+
      [c1.join(['type=button', 'pos=%d,%d,%d,0'%(all_size_x-btn_size-6, all_size_y-0, all_size_x-6), 'cap=Cancel'])]
      )

    res = dlg_custom('Addons Manager options', all_size_x, all_size_y+33, text, id_channel)
    if res is None: return

    id, text = res
    if id!=id_ok: return
    text = text.splitlines()

    ch = text[id_channel].split('\t')
    opt.ch_user = [s for s in ch if s]
    opt.suggest_readme = text[id_readme]=='1'
    opt.install_confirm = text[id_confirm]=='1'
    opt.proxy = text[id_proxy]

    return True
