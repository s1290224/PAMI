import FPFPMiner as alg

obj = alg.FPFPMiner("input.txt", 2, 3)

obj.startMine()

frequentPatterns = obj.getPeriodicFrequentPatterns()

print("Total number of Fuzzy Periodic Frequent Patterns:", len(frequentPatterns))

obj.storePatternsInFile("output.txt")

Df = obj.getPatternsInDataFrame()

memUSS = obj.getMemoryUSS()

print("Total Memory in USS:", memUSS)

memRSS = obj.getMemoryRSS()

print("Total Memory in RSS", memRSS)

run = obj.getRuntime()

print("Total ExecutionTime in seconds:", run)