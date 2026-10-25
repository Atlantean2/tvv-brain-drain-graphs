"""Builds the TechVestVentures Brain Drain Graphs site from the weekly Focus graph collections (focus/weekly/<date>/work/weekly.json, category 'Brain Drain'). Numbers come only from the linked sources."""
import os,sys,shutil
sys.path.insert(0,'/workspace/risk-watcher/graphs-site');sys.path.insert(0,'/workspace/risk-watcher');os.chdir(os.path.dirname(os.path.abspath(__file__)))
import common,weekly_lib as WL
from common import *
T="TechVestVentures Brain Drain Graphs";CAT="Brain Drain"
common.CSS+=WL.GRID_CSS
shutil.rmtree("issues",ignore_errors=True);os.makedirs("issues/img")
tabs=[]
def w(k,lab,body): open(f"issues/{k}.html","w").write(page(T,k,body));tabs.append((k,lab))
NOTE="Weekly Focus graphs, started Oct 25, 2026: new charts are added each week from primary or clearly named secondary data. Each caption names its sources and its caveats."
G=WL.add_tabs(CAT,w,E,save_img,start=1,note=NOTE)
src=WL.sources(CAT)
w("sources","Sources",f'<h2 class="desk">Sources ({len(src)} links)</h2><p>All charts were drawn by TechVestVentures from the data linked below. No numbers were copied from third-party chart images.</p><ul class="src">'+"".join(f'<li>{E(l)}: <a href="{E(u)}">{E(u)}</a></li>' for u,l in src.items())+"</ul>")
index(T,tabs,"Sections",cur="brain");print({k:len(v) for k,v in G.items()},len(src))
