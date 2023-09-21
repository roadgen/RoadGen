from func.printAuto import printAutoInd
def printAsserts(f):
    printAutoInd(f, '% The following are the common parts of the various components.')
    printAutoInd(f, '% We define a new map file and import all possible assets in case of emergency.')
    printAutoInd(f, 'rrMap = roadrunnerHDMap;')
    printAutoInd(f, '')
    printAutoInd(f,
                 'solidwhiteasset = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Markings/SolidSingleWhite.rrlms");')
    printAutoInd(f,
                 'solidyellowasset = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Markings/SolidSingleYellow.rrlms");')
    printAutoInd(f,
                 'dashedwhiteasset = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Markings/DashedSingleWhite.rrlms");')
    printAutoInd(f,
                 'dashedyellowasset = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Markings/DashedSingleYellow.rrlms");')
    printAutoInd(f,
                 'dashedsolidwhiteasset = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Markings/DashedSolidWhite.rrlms");')
    printAutoInd(f,
                 'dashedsolidyellowasset = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Markings/DashedSolidYellow.rrlms");')
    printAutoInd(f,
                 'soliddoublewhiteasset = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Markings/SolidDoubleWhite.rrlms");')
    printAutoInd(f,
                 'soliddoubleyellowasset = roadrunner.hdmap.RelativeAssetPath(AssetPath="Assets/Markings/SolidDoubleYellow.rrlms");')
    printAutoInd(f, '')
    printAutoInd(f, 'markingSpan = [0 1];')
    printAutoInd(f, 'rrMap.LaneMarkings(8,1) = roadrunner.hdmap.LaneMarking();')
    printAutoInd(f,
                 '[rrMap.LaneMarkings.ID] = deal("SolidWhite","SolidYellow","DashedWhite","DashedYellow","DashedSolidWhite","DashedSolidYellow","SolidDoubleWhite","SolidDoubleYellow");')
    printAutoInd(f,
                 '[rrMap.LaneMarkings.AssetPath] = deal(solidwhiteasset,solidyellowasset,dashedwhiteasset,dashedyellowasset,dashedsolidwhiteasset,dashedsolidyellowasset,soliddoublewhiteasset,soliddoubleyellowasset);')
    printAutoInd(f,
                 'markingRefSW = roadrunner.hdmap.MarkingReference(MarkingID=roadrunner.hdmap.Reference(ID="SolidWhite"));')
    printAutoInd(f,
                 'markingAttribSW = roadrunner.hdmap.ParametricAttribution(MarkingReference=markingRefSW,Span=markingSpan);')
    printAutoInd(f,
                 'markingRefSY = roadrunner.hdmap.MarkingReference(MarkingID=roadrunner.hdmap.Reference(ID="SolidYellow"));')
    printAutoInd(f,
                 'markingAttribSY = roadrunner.hdmap.ParametricAttribution(MarkingReference=markingRefSY,Span=markingSpan);')
    printAutoInd(f,
                 'markingRefDW = roadrunner.hdmap.MarkingReference(MarkingID=roadrunner.hdmap.Reference(ID="DashedWhite"));')
    printAutoInd(f,
                 'markingAttribDW = roadrunner.hdmap.ParametricAttribution(MarkingReference=markingRefDW,Span=markingSpan);')
    printAutoInd(f,
                 'markingRefDY = roadrunner.hdmap.MarkingReference(MarkingID=roadrunner.hdmap.Reference(ID="DashedYellow"));')
    printAutoInd(f,
                 'markingAttribDY = roadrunner.hdmap.ParametricAttribution(MarkingReference=markingRefDY,Span=markingSpan);')
    printAutoInd(f,
                 'markingRefDSW = roadrunner.hdmap.MarkingReference(MarkingID=roadrunner.hdmap.Reference(ID="DashedSolidWhite"));')
    printAutoInd(f,
                 'markingAttribDSW = roadrunner.hdmap.ParametricAttribution(MarkingReference=markingRefDSW,Span=markingSpan);')
    printAutoInd(f,
                 'markingRefDSY = roadrunner.hdmap.MarkingReference(MarkingID=roadrunner.hdmap.Reference(ID="DashedSolidYellow"));')
    printAutoInd(f,
                 'markingAttribDSY = roadrunner.hdmap.ParametricAttribution(MarkingReference=markingRefDSY,Span=markingSpan);')
    printAutoInd(f,
                 'markingRefSDW = roadrunner.hdmap.MarkingReference(MarkingID=roadrunner.hdmap.Reference(ID="SolidDoubleWhite"));')
    printAutoInd(f,
                 'markingAttribSDW = roadrunner.hdmap.ParametricAttribution(MarkingReference=markingRefSDW,Span=markingSpan);')
    printAutoInd(f,
                 'markingRefSDY = roadrunner.hdmap.MarkingReference(MarkingID=roadrunner.hdmap.Reference(ID="SolidDoubleYellow"));')
    printAutoInd(f,
                 'markingAttribSDY = roadrunner.hdmap.ParametricAttribution(MarkingReference=markingRefSDY,Span=markingSpan);')