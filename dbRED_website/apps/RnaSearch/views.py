# coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import re
import os
import sys
import subprocess
import datetime
import pickle
# Create your views here.

from .models import Human_Rnaedit, Mouse_Rnaedit, Rat_Rnaedit, Chimpanzee_Rnaedit, Rhesus_Rnaedit, Cbrenneri_Rnaedit, \
    Cbriggsae_Rnaedit, Celegans_Rnaedit, Cjaponica_Rnaedit, Cremanei_Rnaedit, Dananassae_Rnaedit, Dmelanogaster_Rnaedit, \
    Dmojavensis_Rnaedit, Dpseudoobscura_Rnaedit, Dsimulans_Rnaedit, Dvirilis_Rnaedit, Dyakuba_Rnaedit, Project_Cellline

AAChangeTypes = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
AAChangeNum = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}

GeneRegionTypes = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                   'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0, 'downstream': 0, \
                   'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
GeneRegionNum = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                 'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0, 'downstream': 0, \
                 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}

RepeatTypes = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
RepeatNum = {'NonRep': 0, 'Rep': 0, 'Alu': 0}

MethodTypes = {'Single_method': 0, 'Pool_method': 0, 'Giremi': 0, 'DeepRed': 0}
Methoddict = {'Single_method': 'S', 'Pool_method': 'P', 'Giremi': 'G', 'DeepRed': 'D'}
MethodNum = {'Single_method': 0, 'Pool_method': 0, 'Giremi': 0, 'DeepRed': 0}

Human_Project = {'Encode': 0, 'CCLE': 0, 'Roadmap': 0, 'GEUV':0, 'ABRF':0, 'HumanBodyMap':0, 'SEQC':0, 'BrainDataSet':0}
Human_ProjectNum = {'Encode': 0, 'CCLE': 0, 'Roadmap': 0, 'GEUV':0, 'ABRF':0, 'HumanBodyMap':0, 'SEQC':0, 'BrainDataSet':0}

dbSNPTypes = {'yes': 0, 'no': 0}
dbSNPNum = {'yes': 0, 'no': 0}

RnaTypes = {'lncRNA':0, 'circRNA':0, 'miRNA':0, 'piRNA':0}
RnaNum = {'lncRNA':0, 'circRNA':0, 'miRNA':0, 'piRNA':0}


class DetailView(View):
    def get(self, request):
        Chr_pos = request.GET.get("Chr", "")
        Specie = request.GET.get("Specie", "")
        if Chr_pos != '':
            Chr = Chr_pos.split(':')[0]
            pos = Chr_pos.split(':')[1]
        else:
            return render(request, "search.html", {
                "Error_message": "Please pass Chr arg",
            })

        if Specie == 'Human':
            Rnaedit_info = Human_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Mouse':
            Rnaedit_info = Mouse_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Rat':
            Rnaedit_info = Rat_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Rhesus':
            Rnaedit_info = Rhesus_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Chimpanzee':
            Rnaedit_info = Chimpanzee_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Cbrenneri':
            Rnaedit_info = Cbrenneri_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Cbriggsae':
            Rnaedit_info = Cbriggsae_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Celegans':
            Rnaedit_info = Celegans_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Cjaponica':
            Rnaedit_info = Cjaponica_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Cremanei':
            Rnaedit_info = Cremanei_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Dananassae':
            Rnaedit_info = Dananassae_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Dmelanogaster':
            Rnaedit_info = Dmelanogaster_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Dmojavensis':
            Rnaedit_info = Dmojavensis_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Dpseudoobscura':
            Rnaedit_info = Dpseudoobscura_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Dsimulans':
            Rnaedit_info = Dsimulans_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Dvirilis':
            Rnaedit_info = Dvirilis_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        elif Specie == 'Dyakuba':
            Rnaedit_info = Dyakuba_Rnaedit.objects.get(Q(Chr=Chr), Q(position=pos))
        else:
            return render(request, "search.html", {
                "Error_message": "Please pass specie arg",
            })

        Rnaedit_ref_image = Specie + '_' + Chr + '_' + pos + '_ref.png'
        Rnaedit_alt_image = Specie + '_' + Chr + '_' + pos + '_alt.png'
        if not (os.path.exists('/home/zhaochenghui/Rnaedit/static/image/' + Rnaedit_ref_image) and os.path.exists(
                '/home/zhaochenghui/Rnaedit/static/image/' + Rnaedit_alt_image)):
            seq = Rnaedit_info.Sequence
            ref = Rnaedit_info.Ref
            os.chdir('/home/zhaochenghui/Rnaedit/media/tmp')
            subprocess.check_call(
                'python produce_structure.py ' + Specie + ' ' + Chr + ' ' + pos + ' ' + seq + ' ' + ref, shell=True)
        return render(request, "detail_.html", {
            "Specie": Specie,
            "Rnaedit_info": Rnaedit_info,
            "Rnaedit_ref_image": Rnaedit_ref_image,
            "Rnaedit_alt_image": Rnaedit_alt_image,
        })


class StatisticView(View):
    def get(self, request, name):
        if name == 'human':
            return render(request, "statistic_human.html")
        elif name == 'drosophila':
            return render(request, "statistic_drosophila.html")
        elif name == 'mouse':
            return render(request, "statistic_mouse.html")
        elif name == 'rat':
            return render(request, "statistic_rat.html")
        elif name == 'chimpanzee':
            return render(request, "statistic_chimpanzee.html")
        elif name == 'rhesus':
            return render(request, "statistic_rhesus.html")
        elif name == 'nematode':
            return render(request, "statistic_nematode.html")


class StatisticsView(View):
    def get(self, request):
        return render(request, "statistics_all.html")


class ProjectView(View):
    def get(self, request, project):
        title_dict = {"Human_project": "Human", "MouseEncode": "MouseEncode", "C_elegans": "C.elegans",
                      "D_melanogaster": "D.melanogaster"}
        title = title_dict[project]
        return render(request, "project.html", {
            "project": project,
            "title": title
        })


class SearchHomeView(View):
    def get(self, request):
        return render(request, "search.html")

    def post(self, request):
        return render(request, "search.html")


class DownloadView(View):
    def get(self, request):
        return render(request, "download.html")

class HelpView(View):
    def get(self, request):
        return render(request, "help.html")

class SearchView(View):
    def get(self, request):
        AAChangeNum = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
        GeneRegionNum = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                         'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0, 'downstream': 0, \
                         'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
        RepeatNum = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
        MethodNum = {'Single_method': 0, 'Pool_method': 0, 'Giremi': 0, 'DeepRed': 0}
        Human_ProjectNum = {'Encode': 0, 'CCLE': 0, 'Roadmap': 0, 'GEUV': 0, 'ABRF': 0, 'HumanBodyMap': 0, 'SEQC': 0,
                            'BrainDataSet': 0}
        dbSNPNum = {'yes': 0, 'no': 0}
        RnaNum = {'lncRNA': 0, 'circRNA': 0, 'miRNA': 0, 'piRNA': 0}
        # get Rnaedits
        Chr_pos = request.GET.get("Chr", "")
        Specie = request.GET.get("Specie", "")
        Genename = request.GET.get("Genename", "")

        if Chr_pos != '':
            Chr = Chr_pos.split(':')[0]
            pos = Chr_pos.split(':')[1]
            start_pos = int(pos.split('-')[0])
            end_pos = int(pos.split('-')[1])

        if Specie == 'Human':
            if Chr_pos != '':
                RNAedits = Human_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            elif Genename != '':
                # RNAedits = Human_Rnaedit.objects.filter(Q(Genename__icontains=Genename))
                flag = 0
                symbol_list = [",", "(", ".", "-", "_", ":"]
                for symbol in symbol_list:
                    if symbol in Genename:
                        flag += 1
                if flag == 0:
                    command = "match(Genename) against('%s*' in boolean mode)" % Genename
                else:
                    command = "match(Genename) against('\"%s\"' in boolean mode)" % Genename
                RNAedits = Human_Rnaedit.objects.extra(where=[command])
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr or gene arg",
                })
        elif Specie == 'Mouse':
            if Chr_pos != '':
                RNAedits = Mouse_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            elif Genename != '':
                flag = 0
                symbol_list = [",", "(", ".", "-", "_", ":"]
                for symbol in symbol_list:
                    if symbol in Genename:
                        flag += 1
                if flag == 0:
                    command = "match(Genename) against('%s*' in boolean mode)" % Genename
                else:
                    command = "match(Genename) against('\"%s\"' in boolean mode)" % Genename
                RNAedits = Mouse_Rnaedit.objects.extra(where=[command])
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr or gene arg",
                })
        elif Specie == 'Rat':
            if Chr_pos != '':
                RNAedits = Rat_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            elif Genename != '':
                if "." in Genename:
                    search_gene = Genename.split(".")[0]
                else:
                    search_gene = Genename
                command = "match(Genename) against('%s*' in boolean mode)" % search_gene
                RNAedits = Rat_Rnaedit.objects.extra(where=[command])
                # RNAedits = Rat_Rnaedit.objects.filter(Genename__icontains=Genename)
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr or gene arg",
                })
        elif Specie == 'Rhesus':
            if Chr_pos != '':
                RNAedits = Rhesus_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            elif Genename != '':
                if "." in Genename:
                    search_gene = Genename.split(".")[0]
                else:
                    search_gene = Genename
                command = "match(Genename) against('%s*' in boolean mode)" % search_gene
                RNAedits = Rhesus_Rnaedit.objects.extra(where=[command])
                # RNAedits = Rhesus_Rnaedit.objects.filter(Genename__icontains=Genename)
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr or gene arg",
                })
        elif Specie == 'Chimpanzee':
            if Chr_pos != '':
                RNAedits = Chimpanzee_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            elif Genename != '':
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Chimpanzee_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Chimpanzee_Rnaedit.objects.filter(Genename__icontains=Genename)
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr or gene arg",
                })
        elif Specie == 'Cbrenneri':
            if Chr_pos != '':
                RNAedits = Cbrenneri_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr arg, This " + Specie + " doesn't have Genename",
                })
        elif Specie == 'Cbriggsae':
            if Chr_pos != '':
                RNAedits = Cbriggsae_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            elif Genename != '':
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Cbriggsae_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Cbriggsae_Rnaedit.objects.filter(Genename__icontains=Genename)
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr or gene arg",
                })
        elif Specie == 'Celegans':
            if Chr_pos != '':
                RNAedits = Celegans_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            elif Genename != '':
                command = "match(Genename) against('%s+' in boolean mode)" % Genename
                # RNAedits = Celegans_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Celegans_Rnaedit.objects.filter(Genename__icontains=Genename)
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr or gene arg",
                })
        elif Specie == 'Cjaponica':
            if Chr_pos != '':
                RNAedits = Cjaponica_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr arg, This " + Specie + " doesn't have Genename",
                })
        elif Specie == 'Cremanei':
            if Chr_pos != '':
                RNAedits = Cremanei_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr arg, This " + Specie + " doesn't have Genename",
                })
        elif Specie == 'Dananassae':
            if Chr_pos != '':
                RNAedits = Dananassae_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            elif Genename != '':
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Dananassae_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Dananassae_Rnaedit.objects.filter(Genename__icontains=Genename)
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr or gene arg",
                })
        elif Specie == 'Dmelanogaster':
            if Chr_pos != '':
                RNAedits = Dmelanogaster_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            elif Genename != '':
                flag = 0
                symbol_list = [",", "(", ".", "-", "_", ":"]
                for symbol in symbol_list:
                    if symbol in Genename:
                        flag += 1
                if flag == 0:
                    command = "match(Genename) against('%s*' in boolean mode)" % Genename
                else:
                    command = "match(Genename) against('\"%s\"' in boolean mode)" % Genename
                RNAedits = Dmelanogaster_Rnaedit.objects.extra(where=[command])
                # RNAedits = Dmelanogaster_Rnaedit.objects.filter(Genename__icontains=Genename)
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr or gene arg",
                })
        elif Specie == 'Dmojavensis':
            if Chr_pos != '':
                RNAedits = Dmojavensis_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            elif Genename != '':
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Dmojavensis_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Dmojavensis_Rnaedit.objects.filter(Genename__icontains=Genename)
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr or gene arg",
                })
        elif Specie == 'Dpseudoobscura':
            if Chr_pos != '':
                RNAedits = Dpseudoobscura_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            elif Genename != '':
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Dpseudoobscura_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Dpseudoobscura_Rnaedit.objects.filter(Genename__icontains=Genename)
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr or gene arg",
                })
        elif Specie == 'Dsimulans':
            if Chr_pos != '':
                RNAedits = Dsimulans_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            elif Genename != '':
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Dsimulans_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Dsimulans_Rnaedit.objects.filter(Genename__icontains=Genename)
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr or gene arg",
                })
        elif Specie == 'Dvirilis':
            if Chr_pos != '':
                RNAedits = Dvirilis_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            elif Genename != '':
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Dvirilis_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Dvirilis_Rnaedit.objects.filter(Genename__icontains=Genename)
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr or gene arg",
                })
        elif Specie == 'Dyakuba':
            if Chr_pos != '':
                RNAedits = Dyakuba_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            elif Genename != '':
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Dyakuba_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Dyakuba_Rnaedit.objects.filter(Genename__icontains=Genename)
            else:
                return render(request, "search.html", {
                    "Error_message": "Please pass chr or gene arg",
                })
        else:
            return render(request, "search.html", {
                "Error_message": "Please pass specie arg",
            })

        # filter
        AAChange_str = ''
        GeneRegion_str = ''
        Repeat_str = ''
        Project_str = ''
        dbSNP_str = ''
        Rna_str = ''
        # RANedits filter
        # AAChange
        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
            AAChange_list = request.GET.get('AAChange', "")
            AAChange_input = AAChange_list
            AAChange_str = AAChange_list
            if AAChange_list:
                AAChange_list = AAChange_list.split(',')
                RNAedits = RNAedits.filter(AAChange__in=AAChange_list)

        # Repeat
        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei' and Specie != 'Dmojavensis' and Specie != 'Dvirilis':
            Repeat_list = request.GET.get('Location', "")
            Repeat_input = Repeat_list
            Repeat_str = Repeat_list
            if Repeat_list:
                Repeat_list = Repeat_list.split(',')
                RNAedits = RNAedits.filter(Repeat__in=Repeat_list)
        # GeneRegion
        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
            GeneRegion_list = request.GET.get('GeneRegion', "")
            GeneRegion_input = GeneRegion_list
            GeneRegion_str = GeneRegion_list
            if GeneRegion_list:
                GeneRegion_list = GeneRegion_list.split(',')
                RNAedits = RNAedits.filter(GeneRegion__in=GeneRegion_list)
        # Method
        Method_list = request.GET.get('Method', "")
        Method_input = Method_list
        Method_str = Method_list
        if Method_list:
            Method_list = Method_list.split(',')
            Method_list_convert = [Methoddict[i] for i in Method_list]
            condition = Q()
            for i in Method_list_convert:
                condition &= Q(method__icontains=i)
            RNAedits = RNAedits.filter(condition)
        # Project
        if Specie == 'Human':
            Project_list = request.GET.get('Project', "")
            Project_input = Project_list
            Project_str = Project_list
            if Project_list:
                Project_list = ';'.join(Project_list.split(','))
                condition = Q()
                for i in Project_list:
                    condition &= Q(Project__icontains=i)
                RNAedits = RNAedits.filter(condition)
        # Cellline
        Celllines = {}
        CelllineNum = {}
        Cellline_list = request.GET.get('Cellline', "")
        Cellline_input = Cellline_list
        Cellline_str = Cellline_list
        if Cellline_list:
            Cellline_list = Cellline_list.split(',')
            condition = Q()
            for i in Cellline_list:
                condition &= Q(Cellline__icontains=i)
            RNAedits = RNAedits.filter(condition)

        # dbSNP
        if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee':
            dbSNP_list = request.GET.get('dbSNP', "")
            dbSNP_input = dbSNP_list
            dbSNP_str = dbSNP_list
            if dbSNP_list:
                dbSNP_list = dbSNP_list.split(',')
                if 'yes' in dbSNP_list and 'no' not in dbSNP_list:
                    RNAedits = RNAedits.exclude(dbSNP='-')
                elif 'yes' not in dbSNP_list and 'no' in dbSNP_list:
                    RNAedits = RNAedits.filter(dbSNP='-')

        #ncRna
        if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee' or Specie == 'Celegans' or Specie == 'Dmelanogaster':
            Rna_list = request.GET.get('Rna',"")
            Rna_str = Rna_list
            if Rna_list:
                Rna_list = Rna_list.split(",")
                for key in Rna_list:
                    command1 = '%s!=""' % key
                    RNAedits = RNAedits.extra(where=[command1])

        #calculate num
        #AAChange
        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
            for key in AAChangeTypes:
                num = RNAedits.filter(AAChange=key).count()
                AAChangeNum[key] = num
                if key in AAChange_list:
                    AAChangeTypes[key] = 1
                else:
                    AAChangeTypes[key] = 0
        #Repeat
        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei' and Specie != 'Dmojavensis' and Specie != 'Dvirilis':
            for key in RepeatTypes:
                num = RNAedits.filter(Repeat=key).count()
                RepeatNum[key] = num
                if key in Repeat_list:
                    RepeatTypes[key] = 1
                else:
                    RepeatTypes[key] = 0

        #Region
        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
            for key in GeneRegionTypes:
                num = RNAedits.filter(GeneRegion=key).count()
                GeneRegionNum[key] = num
                if key in GeneRegion_list:
                    GeneRegionTypes[key] = 1
                else:
                    GeneRegionTypes[key] = 0

        #Method
        for key in MethodTypes:
            num = RNAedits.filter(method__icontains=Methoddict[key]).count()
            MethodNum[key] = num
            if key in Method_list:
                MethodTypes[key] = 1
            else:
                MethodTypes[key] = 0

        # Project
        if Specie == 'Human':
            for key in Human_Project:
                num = RNAedits.filter(Project__icontains=key).count()
                Human_ProjectNum[key] = num
                if key in Project_list:
                    Human_Project[key] = 1
                else:
                    Human_Project[key] = 0

        #Cellline
        # print Cellline_list
        if Specie != 'Human':
            cels = Project_Cellline.objects.get(project=Specie).cellline
            cels = cels.split(';')
            if Specie == "Dmelanogaster":
                cel_tmp = []
                for each_tmp in cels:
                    if each_tmp != "":
                        cel_tmp.append(each_tmp)
                cels = cel_tmp
            else:
                cels.pop()
            for c in cels:
                if c in Cellline_list:
                    Celllines[c] = 1
                else:
                    Celllines[c] = 0
                num = RNAedits.filter(Cellline__icontains=c).count()
                CelllineNum[c] = num
        else:
            Project_list = request.GET.get('Project', "")
            if Project_list:
                Project_list = Project_list.split(',')
                for p in Project_list:
                    cels = Project_Cellline.objects.get(project=p).cellline
                    cels = cels.split(';')
                    cels.pop()
                    for c in cels:
                        if c in Cellline_list:
                            Celllines[c] = 1
                        else:
                            Celllines[c] = 0
                        num = RNAedits.filter(Cellline__icontains=c).count()
                        CelllineNum[c] = num

        #dbSNP
        if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee':
            for key in dbSNPTypes:
                if key == 'yes':
                    num = RNAedits.exclude(dbSNP='-').count()
                else:
                    num = RNAedits.filter(dbSNP='-').count()
                dbSNPNum[key] = num
                if key in dbSNP_list:
                    dbSNPTypes[key] = 1
                else:
                    dbSNPTypes[key] = 0

        #ncRna
        if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee' or Specie == 'Celegans' or Specie == 'Dmelanogaster':
            for key in RnaTypes:
                command1 = '%s!=""' % key
                num = RNAedits.extra(where=[command1]).count()
                RnaNum[key] = num
                if key in Rna_list:
                    RnaTypes[key] = 1
                else:
                    RnaTypes[key] = 0

        Number = RNAedits.count()
        # Paginator
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(RNAedits, 10, request=request)
        RNAedits = p.page(page)
        return render(request, "result.html", {
            "Chr": Chr_pos,
            "Specie": Specie,
            "Genename": Genename,
            "RNAedits": RNAedits,
            "all_AAChanges": AAChangeTypes,
            "all_locations": RepeatTypes,
            "all_generegions": GeneRegionTypes,
            "all_projects": Human_Project,
            "all_methods": MethodTypes,
            "all_dbsnp": dbSNPTypes,
            "all_celllines": Celllines,
            "all_rna": RnaTypes,
            "number": Number,
            "AAChangeNum": AAChangeNum,
            "AAChange_str": AAChange_str,
            "GeneRegionNum": GeneRegionNum,
            "GeneRegion_str": GeneRegion_str,
            "RepeatNum": RepeatNum,
            "Repeat_str": Repeat_str,
            "MethodNum": MethodNum,
            "Method_str": Method_str,
            "ProjectNum": Human_ProjectNum,
            "Project_str": Project_str,
            "dbSNPNum": dbSNPNum,
            "dbSNP_str": dbSNP_str,
            "CelllineNum": CelllineNum,
            "Cellline_str": Cellline_str,
            "RnaNum": RnaNum,
            "Rna_str": Rna_str
        })


    def post(self, request):
        AAChangeNum = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
        GeneRegionNum = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                         'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0, 'downstream': 0, \
                         'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
        RepeatNum = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
        MethodNum = {'Single_method': 0, 'Pool_method': 0, 'Giremi': 0, 'DeepRed': 0}
        Human_ProjectNum = {'Encode': 0, 'CCLE': 0, 'Roadmap': 0, 'GEUV': 0, 'ABRF': 0, 'HumanBodyMap': 0, 'SEQC': 0,
                            'BrainDataSet': 0}
        dbSNPNum = {'yes': 0, 'no': 0}
        RnaNum = {'lncRNA': 0, 'circRNA': 0, 'miRNA': 0, 'piRNA': 0}
        # get Rnaedits
        Chr_pos_or_Genename = request.POST.get("Chr", "")
        Specie = request.POST.get("Specie", "")
    
        if Chr_pos_or_Genename == '':
            return render(request, "search.html", {
                "Error_message": "Please input query, can't handle None.",
            })
        Chr_pos = ''
        Genename = ''
        pattern = re.compile(r'[a-zA-z0-9\._]+:\d+\-\d+')
        match = pattern.match(Chr_pos_or_Genename)
        if match:
            Chr_pos = Chr_pos_or_Genename
        else:
            Genename = Chr_pos_or_Genename
    
        if Chr_pos != '':
            Chr = Chr_pos.split(':')[0]
            pos = Chr_pos.split(':')[1]
            start_pos = int(pos.split('-')[0])
            end_pos = int(pos.split('-')[1])
    
        if Specie == 'Human':
            if Chr_pos != '':
                RNAedits = Human_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                # RNAedits = Human_Rnaedit.objects.filter(Q(Genename__icontains=Genename))
                flag = 0
                symbol_list = [",", "(", ".", "-", "_", ":"]
                for symbol in symbol_list:
                    if symbol in Genename:
                        flag += 1
                if flag == 0:
                    command = "match(Genename) against('%s*' in boolean mode)" % Genename
                else:
                    command = "match(Genename) against('\"%s\"' in boolean mode)" % Genename
                RNAedits = Human_Rnaedit.objects.extra(where=[command])
        elif Specie == 'Mouse':
            if Chr_pos != '':
                RNAedits = Mouse_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                flag = 0
                symbol_list = [",", "(", ".", "-", "_", ":"]
                for symbol in symbol_list:
                    if symbol in Genename:
                        flag += 1
                if flag == 0:
                    command = "match(Genename) against('%s*' in boolean mode)" % Genename
                else:
                    command = "match(Genename) against('\"%s\"' in boolean mode)" % Genename
                RNAedits = Mouse_Rnaedit.objects.extra(where=[command]).order_by('id')
        elif Specie == 'Rat':
            if Chr_pos != '':
                RNAedits = Rat_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                if "." in Genename:
                    search_gene = Genename.split(".")[0]
                else:
                    search_gene = Genename
                command = "match(Genename) against('%s*' in boolean mode)" % search_gene
                RNAedits = Rat_Rnaedit.objects.extra(where=[command])
                # RNAedits = Rat_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Rhesus':
            if Chr_pos != '':
                RNAedits = Rhesus_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                if "." in Genename:
                    search_gene = Genename.split(".")[0]
                else:
                    search_gene = Genename
                command = "match(Genename) against('%s*' in boolean mode)" % search_gene
                RNAedits = Rhesus_Rnaedit.objects.extra(where=[command])
                # RNAedits = Rhesus_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Chimpanzee':
            if Chr_pos != '':
                RNAedits = Chimpanzee_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Chimpanzee_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Chimpanzee_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Cbrenneri':
            if Chr_pos != '':
                RNAedits = Cbrenneri_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                return render(request, "search.html", {
                    "Error_message": Specie + "'s annotation don't have Genename",
                })
        elif Specie == 'Cbriggsae':
            if Chr_pos != '':
                RNAedits = Cbriggsae_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Cbriggsae_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Cbriggsae_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Celegans':
            if Chr_pos != '':
                RNAedits = Celegans_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                command = "match(Genename) against('%s+' in boolean mode)" % Genename
                # RNAedits = Celegans_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Celegans_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Cjaponica':
            if Chr_pos != '':
                RNAedits = Cjaponica_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                return render(request, "search.html", {
                    "Error_message": Specie + "'s annotation don't have Genename",
                })
        elif Specie == 'Cremanei':
            if Chr_pos != '':
                RNAedits = Cremanei_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                return render(request, "search.html", {
                    "Error_message": Specie + "'s annotation don't have Genename",
                })
        elif Specie == 'Dananassae':
            if Chr_pos != '':
                RNAedits = Dananassae_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Dananassae_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Dananassae_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Dmelanogaster':
            if Chr_pos != '':
                RNAedits = Dmelanogaster_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                flag = 0
                symbol_list = [",", "(", ".", "-", "_", ":"]
                for symbol in symbol_list:
                    if symbol in Genename:
                        flag += 1
                if flag == 0:
                    command = "match(Genename) against('%s*' in boolean mode)" % Genename
                else:
                    command = "match(Genename) against('\"%s\"' in boolean mode)" % Genename
                RNAedits = Dmelanogaster_Rnaedit.objects.extra(where=[command])
                # RNAedits = Dmelanogaster_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Dmojavensis':
            if Chr_pos != '':
                RNAedits = Dmojavensis_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Dmojavensis_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Dmojavensis_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Dpseudoobscura':
            if Chr_pos != '':
                RNAedits = Dpseudoobscura_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Dpseudoobscura_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Dpseudoobscura_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Dsimulans':
            if Chr_pos != '':
                RNAedits = Dsimulans_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Dsimulans_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Dsimulans_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Dvirilis':
            if Chr_pos != '':
                RNAedits = Dvirilis_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Dvirilis_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Dvirilis_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Dyakuba':
            if Chr_pos != '':
                RNAedits = Dyakuba_Rnaedit.objects.filter(Q(Chr=Chr), Q(position__range=[start_pos, end_pos]))
            else:
                command = "match(Genename) against('%s*' in boolean mode)" % Genename
                # RNAedits = Dyakuba_Rnaedit.objects.extra(where=[command]).order_by('id')
                RNAedits = Dyakuba_Rnaedit.objects.filter(Genename__icontains=Genename)

        # filter
        # Cellline
        Celllines = {}
        CelllineNum = {}
        if Specie != 'Human':
            cels = Project_Cellline.objects.get(project=Specie).cellline
            cels = cels.split(';')
            if Specie == "Dmelanogaster":
                cel_tmp = []
                for each_tmp in cels:
                    if each_tmp != "":
                        cel_tmp.append(each_tmp)
                cels = cel_tmp
            else:
                cels.pop()
            for c in cels:
                Celllines[c] = 0
                num = RNAedits.filter(Cellline__icontains=c).count()
                CelllineNum[c] = num
    
        # dbSNP
        if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee':
            for key in dbSNPTypes:
                dbSNPTypes[key] = 0
                if key == 'yes':
                    num = RNAedits.exclude(dbSNP='-').count()
                else:
                    num = RNAedits.filter(dbSNP='-').count()
                dbSNPNum[key] = num
        # Project
        if Specie == 'Human':
            for key in Human_Project:
                Human_Project[key] = 0
                num = RNAedits.filter(Project__icontains=key).count()
                Human_ProjectNum[key] = num
        # AAChange
        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
            for key in AAChangeTypes:
                AAChangeTypes[key] = 0
                num = RNAedits.filter(AAChange=key).count()
                AAChangeNum[key] = num
        # GeneRegion
        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
            for key in GeneRegionTypes:
                GeneRegionTypes[key] = 0
                num = RNAedits.filter(GeneRegion=key).count()
                GeneRegionNum[key] = num
        # Repeat
        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei' and Specie != 'Dmojavensis' and Specie != 'Dvirilis':
            for key in RepeatTypes:
                RepeatTypes[key] = 0
                num = RNAedits.filter(Repeat=key).count()
                RepeatNum[key] = num
        # Method
        for key in MethodTypes:
            MethodTypes[key] = 0
            num = RNAedits.filter(method__icontains=Methoddict[key]).count()
            MethodNum[key] = num
        # RNA
        if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee' or Specie == 'Celegans' or Specie == 'Dmelanogaster':
            for key in RnaTypes:
                RnaTypes[key] = 0
                command1 = '%s!=""' % key
                num = RNAedits.extra(where=[command1]).count()
                RnaNum[key] = num

        Number = RNAedits.count()
        # Paginator
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(RNAedits, 10, request=request)
        RNAedits = p.page(page)
        return render(request, "result.html", {
            "Chr": Chr_pos,
            "Specie": Specie,
            "Genename": Genename,
            "RNAedits": RNAedits,
            "all_AAChanges": AAChangeTypes,
            "all_locations": RepeatTypes,
            "all_generegions": GeneRegionTypes,
            "all_projects": Human_Project,
            "all_methods": MethodTypes,
            "all_dbsnp": dbSNPTypes,
            "all_celllines": Celllines,
            "all_rna":RnaTypes,
            "number": Number,
            "AAChangeNum": AAChangeNum,
            "GeneRegionNum": GeneRegionNum,
            "RepeatNum": RepeatNum,
            "MethodNum": MethodNum,
            "ProjectNum": Human_ProjectNum,
            "dbSNPNum": dbSNPNum,
            "CelllineNum": CelllineNum,
            "RnaNum": RnaNum
        })


class MatrixView(View):
    def get(self, request):
        return render(request, "matrix.html")


class MatrixProjectView(View):
    def get(self, request, matproject):
        if matproject == "matrixhuman":
            return render(request, "matrix_human.html")
        elif matproject == "matrixmouse":
            return render(request, "matrix_mouse.html")
        elif matproject == "matrixrat":
            return render(request, "matrix_rat.html")
        elif matproject == "matrixchimpanzee":
            return render(request, "matrix_chimpanzee.html")
        elif matproject == "matrixrhesus":
            return render(request, "matrix_rhesus.html")
        elif matproject == "matrixnematode":
            return render(request, "matrix_nematode.html")
        elif matproject == "matrixdrosophila":
            return render(request, "matrix_drosophila.html")


class MatrixSearchView(View):
    def get(self, request):
        '''
        list_file1 = open("/home/zhaochenghui/Rnaedit/apps/RnaSearch/par.pickle", "rb")
        par_list = pickle.load(list_file1)
        dict_num = {}
        for Numpar in par_list:
            dbSNPNum = {'yes': 0, 'no': 0}
            RepeatNum = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
            GeneRegionNum = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                             'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0, 'downstream': 0, \
                             'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
            AAChangeNum = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
            Specie = Numpar.split(",")[0]
            Project_input = Numpar.split(",")[1]
            Method_input = Numpar.split(",")[2]
            if Specie == "Dmelanogaster" and len(Numpar.split(",")) > 4:
                Cellline_input = ",".join(Numpar.split(",")[3:])
            else:
                Cellline_input = Numpar.split(",")[3]
            Chr_pos = ""
            Genename = ""
            if Specie == "Human":
                if (Project_input != "") and (Method_input == ""):
                    # RNAedits = Human_Rnaedit.objects.filter(Q(Project__icontains=Project_input),
                    # Q(Cellline__icontains=Cellline_input))
                    command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                    command2 = "match(Project) against('%s*'  in boolean mode)" % Project_input
                    RNAedits = Human_Rnaedit.objects.extra(where=[command1, command2])
                elif (Project_input == "") and (Method_input != ""):
                    # RNAedits = Human_Rnaedit.objects.filter(Q(method__icontains=Method_input),
                    # Q(Cellline__icontains=Cellline_input))
                    command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                    command2 = "method like '%%%%%s%%%%'" % Method_input
                    RNAedits = Human_Rnaedit.objects.extra(where=[command1, command2])
                elif (Project_input != "") and (Method_input != ""):
                    command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                    command2 = "match(Project) against('%s*' in boolean mode)" % Project_input
                    command3 = "method like '%%%%%s%%%%'" % Method_input
                    # RNAedits = Human_Rnaedit.objects.filter(Q(Project__icontains=Project_input) & Q(method__icontains=Method_input) &  Q(Cellline__icontains=Cellline_input))
                    RNAedits = Human_Rnaedit.objects.extra(where=[command1, command2, command3])
                else:
                    command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                    RNAedits = Human_Rnaedit.objects.extra(where=[command1])
            RNAedits_list = list(RNAedits.values())
            for each in RNAedits_list:
                if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee':
                    if each["dbSNP"] == "-":
                        dbSNPNum["no"] += 1
                    else:
                        dbSNPNum["yes"] += 1
                if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                    AAChangeNum[each["AAChange"]] += 1
                    if ";" not in each["GeneRegion"]:
                        GeneRegionNum[each["GeneRegion"]] += 1
                if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei' and Specie != 'Dmojavensis' and Specie != 'Dvirilis':
                    RepeatNum[each["Repeat"]] += 1
            dict_num[Numpar] = {}
            dict_num[Numpar]["dbsnp"] = dbSNPNum
            dict_num[Numpar]["aachange"] = AAChangeNum
            dict_num[Numpar]["region"] = GeneRegionNum
            dict_num[Numpar]["repeat"] = RepeatNum
        list_file2 = open("/home/zhaochenghui/Rnaedit/apps/RnaSearch/dict_num.pickle", "wb")
        pickle.dump(dict_num, list_file2)
        list_file2.close()
        '''
        #####################
        begin1 = datetime.datetime.now()
        flag = request.GET.get("flag", "")
        Numpar = request.GET.get("par", "")
        if Numpar == "":
            return render(request, "matrix.html")
        Specie = Numpar.split(",")[0]
        Project_input = Numpar.split(",")[1]
        Method_input = Numpar.split(",")[2]
        if Specie == "Dmelanogaster" and len(Numpar.split(",")) > 4:
            Cellline_input = ",".join(Numpar.split(",")[3:])
        else:
            Cellline_input = Numpar.split(",")[3]
        Chr_pos = ""
        Genename = ""
        if Specie == "Human":
            if (Project_input != "") and (Method_input == ""):
                # RNAedits = Human_Rnaedit.objects.filter(Q(Project__icontains=Project_input),
                # Q(Cellline__icontains=Cellline_input))
                command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                command2 = "match(Project) against('%s*'  in boolean mode)" % Project_input
                RNAedits = Human_Rnaedit.objects.extra(where=[command1, command2])
            elif (Project_input == "") and (Method_input != ""):
                # RNAedits = Human_Rnaedit.objects.filter(Q(method__icontains=Method_input),
                # Q(Cellline__icontains=Cellline_input))
                command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Human_Rnaedit.objects.extra(where=[command1, command2])
            elif (Project_input != "") and (Method_input != ""):
                command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                command2 = "match(Project) against('%s*' in boolean mode)" % Project_input
                command3 = "method like '%%%%%s%%%%'" % Method_input
                # RNAedits = Human_Rnaedit.objects.filter(Q(Project__icontains=Project_input) & Q(method__icontains=Method_input) &  Q(Cellline__icontains=Cellline_input))
                RNAedits = Human_Rnaedit.objects.extra(where=[command1, command2, command3])
            else:
                command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                RNAedits = Human_Rnaedit.objects.extra(where=[command1])
        elif Specie == 'Mouse':
            if Method_input == "":
                command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                RNAedits = Mouse_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Mouse_Rnaedit.objects.extra(where=[command1, command2])

        elif Specie == 'Rat':
            if Method_input == "":
                command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                RNAedits = Rat_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Rat_Rnaedit.objects.extra(where=[command1, command2])
        elif Specie == 'Rhesus':
            if Method_input == "":
                if "prefrontal cortex" in Numpar:
                    Cellline_input = "Brain, prefrontal cortex"
                command1 = "match(Cellline) against('+\"%s\"+' in boolean mode)" % Cellline_input
                RNAedits = Rhesus_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                if "prefrontal cortex" in Numpar:
                    Cellline_input = "Brain, prefrontal cortex"
                command1 = "match(Cellline) against('+\"%s\"+' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Rhesus_Rnaedit.objects.extra(where=[command1, command2])
        elif Specie == 'Chimpanzee':
            if Method_input == "":
                command1 = "match(Cellline) against('+\"%s\"+' in boolean mode)" % Cellline_input
                RNAedits = Chimpanzee_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                command1 = "match(Cellline) against('+\"%s\"+' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Chimpanzee_Rnaedit.objects.extra(where=[command1, command2])
        elif Specie == 'Cbrenneri':
            if Method_input == "":
                command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                RNAedits = Cbrenneri_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Cbrenneri_Rnaedit.objects.extra(where=[command1, command2])
        elif Specie == 'Cbriggsae':
            if Method_input == "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                RNAedits = Cbriggsae_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Cbriggsae_Rnaedit.objects.extra(where=[command1, command2])
        elif Specie == 'Celegans':
            if Method_input == "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                RNAedits = Celegans_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Celegans_Rnaedit.objects.extra(where=[command1, command2])
        elif Specie == 'Cjaponica':
            if Method_input == "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                RNAedits = Cjaponica_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Cjaponica_Rnaedit.objects.extra(where=[command1, command2])
        elif Specie == 'Cremanei':
            if Method_input == "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                RNAedits = Cremanei_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Cremanei_Rnaedit.objects.extra(where=[command1, command2])
        elif Specie == 'Dananassae':
            if Method_input == "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                RNAedits = Dananassae_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Dananassae_Rnaedit.objects.extra(where=[command1, command2])
        elif Specie == 'Dmelanogaster':
            if Method_input == "":
                command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                #command1 = "Cellline like '%%%%%s%%%%'" % Cellline_input
                RNAedits = Dmelanogaster_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                command1 = "match(Cellline) against('\"%s\"' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Dmelanogaster_Rnaedit.objects.extra(where=[command1, command2])
                #RNAedits = Dmelanogaster_Rnaedit.objects.filter(Q(Cellline__icontains=Cellline_input) & Q(method__icontains=Method_input))
        elif Specie == 'Dmojavensis':
            if Method_input == "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                RNAedits = Dmojavensis_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Dmojavensis_Rnaedit.objects.extra(where=[command1, command2])
        elif Specie == 'Dpseudoobscura':
            if Method_input == "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                RNAedits = Dpseudoobscura_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Dpseudoobscura_Rnaedit.objects.extra(where=[command1, command2])
        elif Specie == 'Dsimulans':
            if Method_input == "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                RNAedits = Dsimulans_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Dsimulans_Rnaedit.objects.extra(where=[command1, command2])
        elif Specie == 'Dvirilis':
            if Method_input == "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                RNAedits = Dvirilis_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Dvirilis_Rnaedit.objects.extra(where=[command1, command2])
        elif Specie == 'Dyakuba':
            if Method_input == "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                RNAedits = Dyakuba_Rnaedit.objects.extra(where=[command1])
            elif Method_input != "":
                command1 = "match(Cellline) against('\"%s\"+' in boolean mode)" % Cellline_input
                command2 = "method like '%%%%%s%%%%'" % Method_input
                RNAedits = Dyakuba_Rnaedit.objects.extra(where=[command1, command2])
        '''
        if RNAedits.count() >= 1000:
            top1000_id = RNAedits.values_list('id', flat=True)[0:1000]
            RNAedits = RNAedits.filter(id__in=list(top1000_id))
        '''
        dbSNPNum = {'yes': 0, 'no': 0}
        RepeatNum = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
        GeneRegionNum = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                         'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                         'downstream': 0, \
                         'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
        AAChangeNum = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
        AAChangeTypes = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
        GeneRegionTypes = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                           'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                           'downstream': 0, \
                           'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
        RepeatTypes = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
        dbSNPTypes = {'yes': 0, 'no': 0}
        end2 = datetime.datetime.now()
        begin_list = datetime.datetime.now()
        #RNAedits_list = list(RNAedits.values())
        end_list = datetime.datetime.now()
        begin2 = datetime.datetime.now()
        if flag == "":
            # filter
            global dbSNPTypes
            global AAChangeTypes
            global GeneRegionTypes
            global RepeatTypes
            for key in dbSNPTypes:
                dbSNPTypes[key] = 0
            for key in AAChangeTypes:
                AAChangeTypes[key] = 0
            for key in GeneRegionTypes:
                GeneRegionTypes[key] = 0
            for key in RepeatTypes:
                RepeatTypes[key] = 0
            if Specie == "Human":
                dbSNPNum = {'yes': 0, 'no': 0}
                RepeatNum = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
                GeneRegionNum = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                                 'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                                 'downstream': 0, \
                                 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
                AAChangeNum = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
                AAChangeTypes = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
                GeneRegionTypes = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                                   'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                                   'downstream': 0, \
                                   'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
                RepeatTypes = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
                dbSNPTypes = {'yes': 0, 'no': 0}
                file_list1 = open("/home/zhaochenghui/Rnaedit/apps/RnaSearch/dict_num.pickle", "rb")
                dict_num = pickle.load(file_list1)
                if Numpar in dict_num:
                    dbSNPNum = dict_num[Numpar]["dbsnp"]
                    AAChangeNum = dict_num[Numpar]["aachange"]
                    GeneRegionNum = dict_num[Numpar]["region"]
                    RepeatNum = dict_num[Numpar]["repeat"]
                else:
                    RNAedits_list = list(RNAedits.values())
                    global dbSNPNum
                    global GeneRegionNum
                    global AAChangeNum
                    global RepeatNum
                    for each in RNAedits_list:
                        if each["dbSNP"] == "-":
                            dbSNPNum["no"] += 1
                        else:
                            dbSNPNum["yes"] += 1
                        AAChangeNum[each["AAChange"]] += 1
                        if ";" not in each["GeneRegion"]:
                            GeneRegionNum[each["GeneRegion"]] += 1
                        RepeatNum[each["Repeat"]] += 1
            else:
                dbSNPNum = {'yes': 0, 'no': 0}
                RepeatNum = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
                GeneRegionNum = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                                 'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                                 'downstream': 0, \
                                 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
                AAChangeNum = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
                AAChangeTypes = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
                GeneRegionTypes = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                                   'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                                   'downstream': 0, \
                                   'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
                RepeatTypes = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
                dbSNPTypes = {'yes': 0, 'no': 0}
                RNAedits_list = list(RNAedits.values())
                global dbSNPNum
                global GeneRegionNum
                global AAChangeNum
                global RepeatNum
                for each in RNAedits_list:
                    if Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee':
                        if each["dbSNP"] == "-":
                            dbSNPNum["no"] += 1
                        else:
                            dbSNPNum["yes"] += 1
                    if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                        AAChangeNum[each["AAChange"]] += 1
                        if ";" not in each["GeneRegion"]:
                            GeneRegionNum[each["GeneRegion"]] += 1
                    if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei' and Specie != 'Dmojavensis' and Specie != 'Dvirilis':
                        RepeatNum[each["Repeat"]] += 1
            Number = RNAedits.count()
            # Paginator
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(RNAedits, 10, request=request)
            RNAedits = p.page(page)
            end3 = datetime.datetime.now()
            time1 = end3 - begin1
            time2 = end2 - begin1
            time3 = end3 - begin2
            time_list = end_list - begin_list
            if "+" in Numpar:
                Numpar = Numpar.replace('+','%2B')
            time3 = Numpar
            return render(request, "matrix_result.html", {
                "Numpar": Numpar,
                "Chr": Chr_pos,
                "Specie": Specie,
                "Genename": Genename,
                "RNAedits": RNAedits,
                "all_AAChanges": AAChangeTypes,
                "all_locations": RepeatTypes,
                "all_generegions": GeneRegionTypes,
                "all_dbsnp": dbSNPTypes,
                "number": Number,
                "AAChangeNum": AAChangeNum,
                "GeneRegionNum": GeneRegionNum,
                "RepeatNum": RepeatNum,
                "dbSNPNum": dbSNPNum,
                "time1": time1,
                "time2": time2,
                "time3": time3,
                "time_list": time_list
            })

        elif flag == "1":
            # filter
            AAChange_str = ''
            GeneRegion_str = ''
            Repeat_str = ''
            Project_str = ''
            dbSNP_str = ''
            AAChange_list = request.GET.get('AAChange', "")
            Repeat_list = request.GET.get('Location', "")
            GeneRegion_list = request.GET.get('GeneRegion', "")
            dbSNP_list = request.GET.get('dbSNP', "")
            dbSNPNum = {'yes': 0, 'no': 0}
            RepeatNum = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
            GeneRegionNum = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                             'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                             'downstream': 0, \
                             'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
            AAChangeNum = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
            AAChangeTypes = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
            GeneRegionTypes = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                               'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                               'downstream': 0, \
                               'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
            RepeatTypes = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
            dbSNPTypes = {'yes': 0, 'no': 0}
            if AAChange_list == "" and Repeat_list == "" and GeneRegion_list == "" and dbSNP_list == "":
                if Specie == "Human":
                    file_list1 = open("/home/zhaochenghui/Rnaedit/apps/RnaSearch/dict_num.pickle", "rb")
                    dict_num = pickle.load(file_list1)
                    if Numpar in dict_num:
                        dbSNPNum = {'yes': 0, 'no': 0}
                        RepeatNum = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
                        GeneRegionNum = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                                         'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                                         'downstream': 0, \
                                         'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
                        AAChangeNum = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
                        AAChangeTypes = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
                        GeneRegionTypes = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                                           'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                                           'downstream': 0, \
                                           'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
                        RepeatTypes = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
                        dbSNPTypes = {'yes': 0, 'no': 0}
                        dbSNPNum = dict_num[Numpar]["dbsnp"]
                        AAChangeNum = dict_num[Numpar]["aachange"]
                        GeneRegionNum = dict_num[Numpar]["region"]
                        RepeatNum = dict_num[Numpar]["repeat"]
                        Number = RNAedits.count()
                    else:
                        # AAChange
                        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                            AAChange_list = request.GET.get('AAChange', "")
                            AAChange_str = AAChange_list
                            if AAChange_list:
                                # AAChange_list = AAChange_list.split(',')
                                RNAedits = RNAedits.filter(AAChange=AAChange_list)
                        # Repeat
                        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei' and Specie != 'Dmojavensis' and Specie != 'Dvirilis':
                            Repeat_list = request.GET.get('Location', "")
                            Repeat_str = Repeat_list
                            if Repeat_list:
                                # Repeat_list = Repeat_list.split(',')
                                RNAedits = RNAedits.filter(Repeat=Repeat_list)
                        # Region
                        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                            GeneRegion_list = request.GET.get('GeneRegion', "")
                            GeneRegion_str = GeneRegion_list
                            if GeneRegion_list:
                                GeneRegion_list = GeneRegion_list.split(',')
                                RNAedits = RNAedits.filter(GeneRegion__in=GeneRegion_list)
                        # dbSNP
                        if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee':
                            dbSNP_list = request.GET.get('dbSNP', "")
                            dbSNP_str = dbSNP_list
                            if dbSNP_list:
                                dbSNP_list = dbSNP_list.split(',')
                                if 'yes' in dbSNP_list and 'no' not in dbSNP_list:
                                    RNAedits = RNAedits.exclude(dbSNP='-')
                                elif 'yes' not in dbSNP_list and 'no' in dbSNP_list:
                                    RNAedits = RNAedits.filter(dbSNP='-')
                        RNAedits_list = list(RNAedits.distinct().values())
                        global dbSNPNum
                        global GeneRegionNum
                        global AAChangeNum
                        global RepeatNum
                        dbSNPNum = {'yes': 0, 'no': 0}
                        RepeatNum = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
                        GeneRegionNum = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                                         'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                                         'downstream': 0, \
                                         'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
                        AAChangeNum = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
                        AAChangeTypes = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
                        GeneRegionTypes = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                                           'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                                           'downstream': 0, \
                                           'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
                        RepeatTypes = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
                        dbSNPTypes = {'yes': 0, 'no': 0}
                        for each in RNAedits_list:
                            if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee':
                                if each["dbSNP"] == "-":
                                    dbSNPNum["no"] += 1
                                else:
                                    dbSNPNum["yes"] += 1
                            if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                                AAChangeNum[each["AAChange"]] += 1
                                if ";" not in each["GeneRegion"]:
                                    GeneRegionNum[each["GeneRegion"]] += 1
                            if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei' and Specie != 'Dmojavensis' and Specie != 'Dvirilis':
                                RepeatNum[each["Repeat"]] += 1
                        # AAChange
                        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                            AAChange_list = AAChange_list.split(',')
                            for key in AAChangeTypes:
                                if key in AAChange_list:
                                    AAChangeTypes[key] = 1
                                else:
                                    AAChangeTypes[key] = 0
                        # Repeat
                        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei' and Specie != 'Dmojavensis' and Specie != 'Dvirilis':
                            Repeat_list = Repeat_list.split(',')
                            for key in RepeatTypes:
                                if key in Repeat_list:
                                    RepeatTypes[key] = 1
                                else:
                                    RepeatTypes[key] = 0
                        # GeneRegion
                        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                            for key in GeneRegionTypes:
                                if key in GeneRegion_list:
                                    GeneRegionTypes[key] = 1
                                else:
                                    GeneRegionTypes[key] = 0
                        # dbSNP
                        if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee':
                            for key in dbSNPTypes:
                                if key in dbSNP_list:
                                    dbSNPTypes[key] = 1
                                else:
                                    dbSNPTypes[key] = 0
                        Number = len(RNAedits_list)
                else:
                    # AAChange
                    if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                        AAChange_list = request.GET.get('AAChange', "")
                        AAChange_str = AAChange_list
                        if AAChange_list:
                            # AAChange_list = AAChange_list.split(',')
                            RNAedits = RNAedits.filter(AAChange=AAChange_list)
                    # Repeat
                    if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei' and Specie != 'Dmojavensis' and Specie != 'Dvirilis':
                        Repeat_list = request.GET.get('Location', "")
                        Repeat_str = Repeat_list
                        if Repeat_list:
                            # Repeat_list = Repeat_list.split(',')
                            RNAedits = RNAedits.filter(Repeat=Repeat_list)
                    # Region
                    if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                        GeneRegion_list = request.GET.get('GeneRegion', "")
                        GeneRegion_str = GeneRegion_list
                        if GeneRegion_list:
                            GeneRegion_list = GeneRegion_list.split(',')
                            RNAedits = RNAedits.filter(GeneRegion__in=GeneRegion_list)
                    # dbSNP
                    if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee':
                        dbSNP_list = request.GET.get('dbSNP', "")
                        dbSNP_str = dbSNP_list
                        if dbSNP_list:
                            dbSNP_list = dbSNP_list.split(',')
                            if 'yes' in dbSNP_list and 'no' not in dbSNP_list:
                                RNAedits = RNAedits.exclude(dbSNP='-')
                            elif 'yes' not in dbSNP_list and 'no' in dbSNP_list:
                                RNAedits = RNAedits.filter(dbSNP='-')
                    RNAedits_list = list(RNAedits.distinct().values())
                    global dbSNPNum
                    global GeneRegionNum
                    global AAChangeNum
                    global RepeatNum
                    dbSNPNum = {'yes': 0, 'no': 0}
                    RepeatNum = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
                    GeneRegionNum = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                                     'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                                     'downstream': 0, \
                                     'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
                    AAChangeNum = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
                    AAChangeTypes = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
                    GeneRegionTypes = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                                       'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                                       'downstream': 0, \
                                       'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
                    RepeatTypes = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
                    dbSNPTypes = {'yes': 0, 'no': 0}
                    for each in RNAedits_list:
                        if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee':
                            if each["dbSNP"] == "-":
                                dbSNPNum["no"] += 1
                            else:
                                dbSNPNum["yes"] += 1
                        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                            AAChangeNum[each["AAChange"]] += 1
                            if ";" not in each["GeneRegion"]:
                                GeneRegionNum[each["GeneRegion"]] += 1
                        if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei' and Specie != 'Dmojavensis' and Specie != 'Dvirilis':
                            RepeatNum[each["Repeat"]] += 1
                    # AAChange
                    if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                        AAChange_list = AAChange_list.split(',')
                        for key in AAChangeTypes:
                            if key in AAChange_list:
                                AAChangeTypes[key] = 1
                            else:
                                AAChangeTypes[key] = 0
                    # Repeat
                    if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei' and Specie != 'Dmojavensis' and Specie != 'Dvirilis':
                        Repeat_list = Repeat_list.split(',')
                        for key in RepeatTypes:
                            if key in Repeat_list:
                                RepeatTypes[key] = 1
                            else:
                                RepeatTypes[key] = 0
                    # GeneRegion
                    if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                        for key in GeneRegionTypes:
                            if key in GeneRegion_list:
                                GeneRegionTypes[key] = 1
                            else:
                                GeneRegionTypes[key] = 0
                    # dbSNP
                    if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee':
                        for key in dbSNPTypes:
                            if key in dbSNP_list:
                                dbSNPTypes[key] = 1
                            else:
                                dbSNPTypes[key] = 0
                    Number = len(RNAedits_list)

            else:
                # AAChange
                if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                    AAChange_list = request.GET.get('AAChange', "")
                    AAChange_str = AAChange_list
                    if AAChange_list:
                        #AAChange_list = AAChange_list.split(',')
                        RNAedits = RNAedits.filter(AAChange=AAChange_list)
                #Repeat
                if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei' and Specie != 'Dmojavensis' and Specie != 'Dvirilis':
                    Repeat_list = request.GET.get('Location', "")
                    Repeat_str = Repeat_list
                    if Repeat_list:
                        #Repeat_list = Repeat_list.split(',')
                        RNAedits = RNAedits.filter(Repeat=Repeat_list)
                #Region
                if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                    GeneRegion_list = request.GET.get('GeneRegion', "")
                    GeneRegion_str = GeneRegion_list
                    if GeneRegion_list:
                        GeneRegion_list = GeneRegion_list.split(',')
                        RNAedits = RNAedits.filter(GeneRegion__in=GeneRegion_list)
                #dbSNP
                if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee':
                    dbSNP_list = request.GET.get('dbSNP', "")
                    dbSNP_str = dbSNP_list
                    if dbSNP_list:
                        dbSNP_list = dbSNP_list.split(',')
                        if 'yes' in dbSNP_list and 'no' not in dbSNP_list:
                            RNAedits = RNAedits.exclude(dbSNP='-')
                        elif 'yes' not in dbSNP_list and 'no' in dbSNP_list:
                            RNAedits = RNAedits.filter(dbSNP='-')
                RNAedits_list = list(RNAedits.distinct().values())
                global dbSNPNum
                global GeneRegionNum
                global AAChangeNum
                global RepeatNum
                dbSNPNum = {'yes': 0, 'no': 0}
                RepeatNum = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
                GeneRegionNum = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                                 'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                                 'downstream': 0, \
                                 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
                AAChangeNum = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
                AAChangeTypes = {'unknown': 0, 'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0}
                GeneRegionTypes = {'intergenic': 0, 'upstream': 0, 'ncRNA_exonic': 0, 'ncRNA_intronic': 0, \
                                   'UTR3': 0, 'intronic': 0, 'ncRNA_splicing': 0, 'UTR5': 0, 'splicing': 0,
                                   'downstream': 0, \
                                   'nonsynonymous SNV': 0, 'synonymous SNV': 0, 'stoploss': 0, 'unknown': 0}
                RepeatTypes = {'NonRep': 0, 'Rep': 0, 'Alu': 0}
                dbSNPTypes = {'yes': 0, 'no': 0}
                for each in RNAedits_list:
                    if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee':
                        if each["dbSNP"] == "-":
                            dbSNPNum["no"] += 1
                        else:
                            dbSNPNum["yes"] += 1
                    if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                        AAChangeNum[each["AAChange"]] += 1
                        if ";" not in each["GeneRegion"]:
                            GeneRegionNum[each["GeneRegion"]] += 1
                    if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei' and Specie != 'Dmojavensis' and Specie != 'Dvirilis':
                        RepeatNum[each["Repeat"]] += 1
                # AAChange
                if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                    AAChange_list = AAChange_list.split(',')
                    for key in AAChangeTypes:
                        if key in AAChange_list:
                            AAChangeTypes[key] = 1
                        else:
                            AAChangeTypes[key] = 0
                # Repeat
                if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei' and Specie != 'Dmojavensis' and Specie != 'Dvirilis':
                    Repeat_list = Repeat_list.split(',')
                    for key in RepeatTypes:
                        if key in Repeat_list:
                            RepeatTypes[key] = 1
                        else:
                            RepeatTypes[key] = 0
                # GeneRegion
                if Specie != 'Cbrenneri' and Specie != 'Cjaponica' and Specie != 'Cremanei':
                    for key in GeneRegionTypes:
                        if key in GeneRegion_list:
                            GeneRegionTypes[key] = 1
                        else:
                            GeneRegionTypes[key] = 0
                # dbSNP
                if Specie == 'Human' or Specie == 'Mouse' or Specie == 'Rat' or Specie == 'Rhesus' or Specie == 'Chimpanzee':
                    for key in dbSNPTypes:
                        if key in dbSNP_list:
                            dbSNPTypes[key] = 1
                        else:
                            dbSNPTypes[key] = 0
                Number = len(RNAedits_list)
            # Paginator
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
            p = Paginator(RNAedits, 10, request=request)
            RNAedits = p.page(page)
            end3 = datetime.datetime.now()
            time3 = end3 - begin1
            if "+" in Numpar:
                Numpar = Numpar.replace('+','%2B')
            time3 = Numpar
            return render(request, "matrix_result.html", {
                "Numpar": Numpar,
                "Chr": Chr_pos,
                "Specie": Specie,
                "Genename": Genename,
                "RNAedits": RNAedits,
                "all_AAChanges": AAChangeTypes,
                "all_locations": RepeatTypes,
                "all_generegions": GeneRegionTypes,
                "all_dbsnp": dbSNPTypes,
                "number": Number,
                "AAChangeNum": AAChangeNum,
                "AAChange_str": AAChange_str,
                "GeneRegionNum": GeneRegionNum,
                "GeneRegion_str": GeneRegion_str,
                "RepeatNum": RepeatNum,
                "Repeat_str": Repeat_str,
                "dbSNPNum": dbSNPNum,
                "dbSNP_str": dbSNP_str,
                "time3": time3
            })