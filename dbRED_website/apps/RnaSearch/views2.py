#coding:utf-8
from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import re
import os
import sys
import subprocess
# Create your views here.

from .models import Human_Rnaedit, Mouse_Rnaedit, Rat_Rnaedit, Chimpanzee_Rnaedit, Rhesus_Rnaedit, Cbrenneri_Rnaedit, Cbriggsae_Rnaedit, Celegans_Rnaedit, Cjaponica_Rnaedit, Cremanei_Rnaedit, Dananassae_Rnaedit, Dmelanogaster_Rnaedit, Dmojavensis_Rnaedit, Dpseudoobscura_Rnaedit, Dsimulans_Rnaedit, Dvirilis_Rnaedit, Dyakuba_Rnaedit

AAChangeTypes = {'unknown':0, 'nonsynonymous SNV':0, 'synonymous SNV':0, 'stoploss':0}
GeneRegionTypes = {'intergenic':0, 'upstream':0, 'ncRNA_exonic':0, 'ncRNA_intronic':0,\
'UTR3':0, 'intronic':0, 'ncRNA_splicing':0, 'UTR5':0, 'splicing':0, 'downstream':0,\
'nonsynonymous SNV':0, 'synonymous SNV':0, 'stoploss':0, 'unknown':0}
RepeatTypes = {'NonRep':0, 'Rep':0, 'Alu':0}
MethodTypes = {'Jinbilly_single':0, 'Jinbilly_pool':0, 'Giremi':0, 'DeepRed':0}
Methoddict = {'Jinbilly_single':'S', 'Jinbilly_pool':'P', 'Giremi':'G', 'DeepRed':'D'}
Human_Project = {'Encode':0, 'CCLE':0, 'Roadmap':0}
dbSNPTypes = {'yes':0, 'no':0}


class DetailView(View):
    def get(self, request):
        Chr_pos = request.GET.get("Chr", "")
        Specie = request.GET.get("Specie", "")
        if Chr_pos != '':
            Chr = Chr_pos.split(':')[0]
            pos = Chr_pos.split(':')[1]
        else:
            return render(request, "search.html", {
            "Error_message":"Please pass Chr arg",
            })
        
        if Specie == 'Human':
            Rnaedit_info = Human_Rnaedit.objects.get(Q(Chr=Chr),Q(position=pos))
            Rnaedit_ref_image = Specie+'_'+Chr+'_'+pos+'_ref.png'
            Rnaedit_alt_image = Specie+'_'+Chr+'_'+pos+'_alt.png'
            if not(os.path.exists('/home/zhaochenghui/Rnaedit/static/image/'+Rnaedit_ref_image) and os.path.exists('/home/zhaochenghui/Rnaedit/static/image/'+Rnaedit_alt_image)):
                seq = Rnaedit_info.Sequence
                ref = Rnaedit_info.Ref
                os.chdir('/home/zhaochenghui/Rnaedit/media/tmp')
                subprocess.check_call('python produce_structure.py '+Specie+' '+Chr+' '+pos+' '+seq+' '+ref, shell=True)
        else:
            return render(request, "search.html", {
            "Error_message":"Please pass specie arg",
            })
        return render(request, "detail.html", {
            "Specie":Specie,
            "Rnaedit_info":Rnaedit_info,
            "Rnaedit_ref_image":Rnaedit_ref_image,
            "Rnaedit_alt_image":Rnaedit_alt_image,
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
        return render(request, "project.html",{
            "project":project,
        })


class SearchHomeView(View):
    def get(self, request):
        return render(request, "search.html")

    def post(self, request):
        return render(request, "search.html")

class SearchView(View):
    def get(self, request):
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
                RNAedits = Human_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            elif Genename != '':
                RNAedits = Human_Rnaedit.objects.filter(Genename__icontains=Genename)
            else:
                return render(request, "search.html", {
                "Error_message":"Please pass chr or gene arg",    
                })
        else:
            return render(request, "search.html", {
            "Error_message":"Please pass specie arg",
            })

        AAChange_list = request.GET.get('AAChange',"")
        AAChange_str = AAChange_list
        if AAChange_list:
            AAChange_list = AAChange_list.split(',')
            RNAedits = RNAedits.filter(AAChange__in = AAChange_list)
            for key in AAChangeTypes:
                if key in AAChange_list:
                    AAChangeTypes[key] = 1
                else:
                    AAChangeTypes[key] = 0
        else:
            for key in AAChangeTypes:
                if key in AAChange_list:
                    AAChangeTypes[key] = 1
                else:
                    AAChangeTypes[key] = 0

        GeneRegion_list = request.GET.get('GeneRegion', "")
        GeneRegion_str = GeneRegion_list
        if GeneRegion_list:
            GeneRegion_list = GeneRegion_list.split(',')
            RNAedits = RNAedits.filter(GeneRegion__in = GeneRegion_list)
            for key in GeneRegionTypes:
                if key in GeneRegion_list:
                    GeneRegionTypes[key] = 1
                else:
                    GeneRegionTypes[key] = 0
        else:
            for key in GeneRegionTypes:
                if key in GeneRegion_list:
                    GeneRegionTypes[key] = 1
                else:
                    GeneRegionTypes[key] = 0


        Repeat_list = request.GET.get('Location', "")
        Repeat_str = Repeat_list
        if Repeat_list:
            Repeat_list = Repeat_list.split(',')
            RNAedits = RNAedits.filter(Repeat__in = Repeat_list)
            for key in RepeatTypes:
                if key in Repeat_list:
                    RepeatTypes[key] = 1
                else:
                    RepeatTypes[key] = 0
        else:
            for key in RepeatTypes:
                if key in Repeat_list:
                    RepeatTypes[key] = 1
                else:
                    RepeatTypes[key] = 0

        Method_list = request.GET.get('Method', "")
        Method_str = Method_list
        if Method_list:
            Method_list = Method_list.split(',')
            for key in MethodTypes:
                if key in Method_list:
                    MethodTypes[key] = 1
                else:
                    MethodTypes[key] = 0
            Method_list = [Methoddict[i] for i in Method_list]
            condition = Q()
            for i in Method_list:
                condition |= Q(method__icontains = i)
            RNAedits = RNAedits.filter(condition)

        else:
            for key in MethodTypes:
                if key in Method_list:
                    MethodTypes[key] = 1
                else:
                    MethodTypes[key] = 0

        Project_list = request.GET.get('Project', "")
        Project_str = Project_list
        if Project_list:
            Project_list = ';'.join(Project_list.split(','))
            RNAedits = RNAedits.filter(Project__icontains = Project_list)
            for key in Human_Project:
                if key in Project_list:
                    Human_Project[key] = 1
                else:
                    Human_Project[key] = 0
        else:
            for key in Human_Project:
                if key in Project_list:
                    Human_Project[key] = 1
                else:
                    Human_Project[key] = 0

        dbSNP_list = request.GET.get('dbSNP', "")
        dbSNP_str = dbSNP_list
        if dbSNP_list:
            dbSNP_list = dbSNP_list.split(',')
            if 'yes' in dbSNP_list and 'no' not in dbSNP_list:
                RNAedits = RNAedits.exclude(dbSNP = '-')
            elif 'yes' not in dbSNP_list and 'no' in dbSNP_list:
                RNAedits = RNAedits.filter(dbSNP = '-')
            for key in dbSNPTypes:
                if key in dbSNP_list:
                    dbSNPTypes[key] = 1
                else:
                    dbSNPTypes[key] = 0
        else:
            for key in dbSNPTypes:
                if key in dbSNP_list:
                    dbSNPTypes[key] = 1
                else:
                    dbSNPTypes[key] = 0

        Number = RNAedits.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(RNAedits, 10, request=request)

        RNAedits = p.page(page)
        return render(request, "result.html", {
            "Chr":Chr_pos,
            "Specie":Specie,
            "Genename":Genename,
            "RNAedits":RNAedits,
            "all_AAChanges":AAChangeTypes,
            "all_locations":RepeatTypes,
            "all_generegions":GeneRegionTypes,
            "all_projects":Human_Project,
            "all_methods":MethodTypes,
            "all_dbsnp":dbSNPTypes,
            "number":Number,
            "AAChange_str":AAChange_str,
            "GeneRegion_str":GeneRegion_str,
            "Repeat_str":Repeat_str,
            "Method_str":Method_str,
            "Project_str":Project_str,
            "dbSNP_str":dbSNP_str,
            })

    def post(self, request):
        Chr_pos_or_Genename = request.POST.get("Chr", "")
        Specie = request.POST.get("Specie", "")
        
        if Chr_pos_or_Genename == '':
            return render(request, "search.html", {
            "Error_message":"Please input query, can't handle None.",
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
                RNAedits = Human_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Human_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Mouse':
            if Chr_pos != '':
                RNAedits = Mouse_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Mouse_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Rat':
            if Chr_pos != '':
                RNAedits = Rat_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Rat_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Rhesus':
            if Chr_pos != '':
                RNAedits = Rhesus_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Rhesus_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Chimpanzee':
            if Chr_pos != '':
                RNAedits = Chimpanzee_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Chimpanzee_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Cbrenneri':
            if Chr_pos != '':
                RNAedits = Cbrenneri_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Cbrenneri_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Cbriggsae':
            if Chr_pos != '':
                RNAedits = Cbriggsae_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Cbriggsae_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Celegans':
            if Chr_pos != '':
                RNAedits = Celegans_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Celegans_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Cjaponica':
            if Chr_pos != '':
                RNAedits = Cjaponica_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Cjaponica_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Cremanei':
            if Chr_pos != '':
                RNAedits = Cremanei_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Cremanei_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Dananassae':
            if Chr_pos != '':
                RNAedits = Dananassae_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Dananassae_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Dmelanogaster':
            if Chr_pos != '':
                RNAedits = Dmelanogaster_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Dmelanogaster_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Dmojavensis':
            if Chr_pos != '':
                RNAedits = Dmojavensis_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Dmojavensis_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Dpseudoobscura':
            if Chr_pos != '':
                RNAedits = Dpseudoobscura_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Dpseudoobscura_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Dsimulans':
            if Chr_pos != '':
                RNAedits = Dsimulans_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Dsimulans_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Dvirilis':
            if Chr_pos != '':
                RNAedits = Dvirilis_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Dvirilis_Rnaedit.objects.filter(Genename__icontains=Genename)
        elif Specie == 'Dyakuba':
            if Chr_pos != '':
                RNAedits = Dyakuba_Rnaedit.objects.filter(Q(Chr=Chr),Q(position__range=[start_pos,end_pos]))
                if Genename:
                    RNAedits = RNAedits.filter(Genename__icontains=Genename)
            else:
                RNAedits = Dyakuba_Rnaedit.objects.filter(Genename__icontains=Genename)
 
        Number = RNAedits.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(RNAedits, 10, request=request)

        RNAedits = p.page(page)
        return render(request, "result.html", {
            "Chr":Chr_pos,
            "Specie":Specie,
            "Genename":Genename,
            "RNAedits":RNAedits,
            "all_AAChanges":AAChangeTypes,
            "all_locations":RepeatTypes,
            "all_generegions":GeneRegionTypes,
            "all_projects":Human_Project,
            "all_methods":MethodTypes,
            "all_dbsnp":dbSNPTypes,
            "number":Number,
        })
