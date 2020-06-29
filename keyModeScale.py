

class ModesAndScales():
    sharps = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    flats = ['C','D♭','D','E♭','E','F','G♭','G','A♭','A','B♭','B']
    ordered_Notes = None
    mode_Select = None
    
    def getOrder(self, note):
        pos = None
        notes = None
        if note in self.sharps:
            notes = self.sharps
        if note in self.flats:
            notes = self.flats
        
        for i in range(len(notes)):
            if notes[i] == note:
                pos = i
        sect_one = notes[pos:]
        sect_two = notes[:pos + 1]
        self.ordered_Notes = sect_one + sect_two
    
    def select_mode(self, select):
        if select.title() == "Ionian":
            self.mode_Select = Mode.Ionian
        if select.title() == "Dorian":
            self.mode_Select = Mode.Dorian
        if select.title() == "Pyrygain":
            self.mode_Select = Mode.Pyrygain
        if select.title() == "Lydian":
            self.mode_Select = Mode.Lydian
        if select.title() == "Mixolydian":
            self.mode_Select = Mode.Mixolydian
        if select.title() == "Aeolian":
            self.mode_Select = Mode.Aeolian
        if select.title() == "Locrain":
            self.mode_Select = Mode.Locrain

    def get_scale(self):
        mode = self.mode_Select
        notes = self.ordered_Notes
        scale = []
        for i in mode:
            scale.append(notes[i])
        print(scale)

class Mode:
    Ionian = [0,2,4,5,7,9,11,12]
    Dorian = [0,2,3,5,7,9,10,12]
    Pyrygain = [0,1,3,5,7,8,10,12]
    Lydian = [0,2,4,6,7,9,11,12]
    Mixolydian = [0,2,4,5,7,9,10,12]
    Aeolian = [0,2,3,5,7,8,10,12]
    Locrain = [0,1,3,5,6,8,10,12]


if __name__ == '__main__':
    t = ModesAndScales()
    t.getOrder('D#')
    t.select_mode('Aeolian')
    t.get_scale()
   