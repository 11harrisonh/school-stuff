sBlock = [[["H","Hydrogen"],["He","Helium"]],[["Li","Lithium"],["Be","Beryllium"]],[["Na","Sodium"],["Mg","Magnesium"]],[["K","Potassium"],["Ca","Calcium"]],[["Rb","Rubidium"],["Sr","Strontium"]],[["Cs","Caesium"],["Ba","Barium"]],[["Fr","Francium"],["Ra","Radium"]]]
fBlock = [[["La","Lanthanum"],["Ce","Cerium"],["Pr","Praseodymium"],["Nd","Neodymium"],["Pm","Promethium"],["Sm","Samarium"],["Eu","Europium"],["Gd","Gadolinium"],["Tb","Terbium"],["Dy","Dysprosium"],["Ho","Holmium"],["Er","Erbium"],["Tm","Thulium"],["Yb","Ytterbium"]],[["Ac","Actinium"],["Th","Thorium"],["Pa","Protactinium"],["U","Uranium"],["Np","Neptunium"],["Pu","Plutonium"],["Am","Americium"],["Cm","Curium"],["Bk","Berkelium"],["Cf","Californium"],["Es","Einsteinium"],["Fm","Fermium"],["Md","Mendelevium"],["No","Nobelium"]]]
dBlock = [[["Sc","Scandium"],["Ti","Titanium"],["V","Vanadium"],["Cr","Chromium"],["Mn","Manganese"],["Fe","Iron"],["Co","Cobalt"],["Ni","Nickel"],["Cu","Copper"],["Zn","Zinc"]],[["Y","Yttrium"],["Zr","Zirconium"],["Nb","Niobium"],["Mo","Molybdenum"],["Tc","Technetium"],["Ru","Ruthenium"],["Rh","Rhodium"],["Pd","Palladium"],["Ag","Silver"],["Cd","Cadmium"]],[["Lu","Lutetium"],["Hf","Hafnium"],["Ta","Tantalum"],["W","Tungsten"],["Re","Rhenium"],["Os","Osmium"],["Ir","Iridium"],["Pt","Platinum"],["Au","Gold"],["Hg","Mercury"]],[["Lr","Lawrencium"],["Rf","Rutherfordium"],["Db","Dubnium"],["Sg","Seaborgium"],["Bh","Bohrium"],["Hs","Hassium"],["Mt","Meitnerium"],["Ds","Darmstadtium"],["Rg","Roentgenium"],["Cn","Copernicium"]]]
pBlock = [[["B","Boron"],["C","Carbon"],["N","Nitrogen"],["O","Oxygen"],["F","Fluorine"],["Ne","Neon"]],[["Al","Aluminium"],["Si","Silicon"],["P","Phosphorus"],["S","Sulfur"],["Cl","Chlorine"],["Ar","Argon"]],[["Ga","Gallium"],["Ge","Germanium"],["As""Arsenic"],["Se","Selenium"],["Br","Bromine"],["Kr","Krypton"]],[["In","Indium"],["Sn","Tin"],["Sb","Antimony"],["Te","Tellurium"],["I","Iodine"],["Xe","Xenon"]],[["Tl","Thallium"],["Pb","Lead"],["Bi","Bismuth"],["Po","Polonium"],["At","Astatine"],["Rn","Radon"]],[["Uut","Ununtrium"],["Fl","Flerovium"],["Uup","Ununpentium"],["Lv","Livermorium"],["Uus","Ununseptium"],["Uuo","Ununoctium"]]]
allBlocks = [sBlock,fBlock,dBlock,pBlock]

#info = atomic number, melting point, mass number (of most stable isotope)
sBlockInfo = []
fBlockInfo = []
dBlockInfo = []
pBlockInfo = []
allBlockInfo = [sBlockInfo,fBlockInfo,dBlockInfo]
endProgram = False
while endProgram == False:
    query = "{}".format(raw_input("Enter a chemical element (name/symbol): "))
    print("Your query was: {}".format(query))
    print("\nFinding element...")
    endProgram = False
    queryMet = False
    for blockcount in allBlocks:
        for dim1 in blockcount:
            for dim2 in dim1:
                for dim3 in dim2:
                    if query in dim2:
                        print("Found!")
                        queryMet = True
                        break
                    else:
                        continue
                if queryMet:
                    break
            if queryMet:
                break
        if queryMet:
            break
    if queryMet:
        print("\nThe element you searched for was {}".format(dim2[1]))
        print("It can be represented by the chemical symbol {}".format(dim2[0]))
    else:
        print("Sorry, your element was not found. Please make sure it is capitalised and spelled correctly")
    askContinue = str(raw_input("Press enter to end the program, or type 'y' to continue the program: "))
    if askContinue != "y":
        break





print("End")
