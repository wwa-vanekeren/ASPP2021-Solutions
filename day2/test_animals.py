#!/usr/bin/env python
# 1a-e
# import animals

# m = animals.Mammals()
# m.printMembers()

# b = animals.Birds()
# b.printMembers()

# f = animals.Fish()
# f.printMembers()

#1f
import animals

harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printMembers()

mammals = animals.Mammals()
mammals.printMembers()