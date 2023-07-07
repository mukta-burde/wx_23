def findOnePeak(dataFrame, thresHeight, windLength, polyOrder): # Peak Finding Algorithm, user defined params
    g = 0
    for DFI in range(0, dataFrame.size - 1):
        maxPeak = 0
        residuals = [] # array of each residual height from 0 (distance from discrete smoothened yvalue of each sample to 0)
        heightsAboveThreshold = [] # array of values of all discrete smoothened yvalues above threshold height
        halfIndices = [] # array of values with discrete smoothened yvalue exactly (or nearest to) 1/2 of yvalue of peak
        sortedNearest = [] # halfIndices array sorted from smoothened yvalues nearest to 1/2 of yvalue of smoothened peak
        time1 = 0
        time2 = 0
        area = 0
        
        for i in range(0, 2199):
            residuals.append(((savgol_filter(dataframe[DFI], windLength, polyOrder))[i]))
            if residuals[i] > thresHeight:
                heightsAboveThreshold.append(residuals[i]) 
                
        heightsAboveThreshold = np.array(heightsAboveThreshold)
                
        if heightsAboveThreshold.size != 0:
            for r in residuals:
                 if r > maxPeak:
                     maxPeak = r
        
            sortedNearest = sorted(savgol_filter(dataframe[DFI], windLength, polyOrder), key=lambda i: abs(i - (savgol_filter(dataframe[DFI], windLength, polyOrder)[residuals.index(maxPeak)])/ 2))[:3]
            plt.figure(figsize=(20,20))
            g += 1
            plt.subplot(5, 8, g)
            plt.plot(x_data, dataframe[DFI], 'r')
            plt.plot(x_data, savgol_filter(dataframe[DFI], windowLength, polyOrder), 'b')
            plt.plot((residuals.index(maxPeak) * 11)/2200 - 0.5, (savgol_filter(dataframe[DFI], windowLength, polyOrder))[residuals.index(maxPeak)], 'bo')  
            plt.plot((residuals.index(sortedNearest[0]) * 11)/2200 - 0.5, (savgol_filter(dataframe[DFI], windowLength, polyOrder))[residuals.index(sortedNearest[0])], 'bo')
            plt.plot((residuals.index(sortedNearest[1]) * 11)/2200 - 0.5, (savgol_filter(dataframe[DFI], windowLength, polyOrder))[residuals.index(sortedNearest[1])], 'bo')
            
            time1 = ((residuals.index(sortedNearest[0]) * 11)/2200 - 0.5)
            time2 = ((residuals.index(sortedNearest[1]) * 11)/2200 - 0.5)
            
            area = (time2 - time1) * maxPeak
            
            print(f"Peak of value {area} found between time points {time1} and {time2} in BLM {DFI}")
        else:  
            print(f"No peaks found at BLM {DFI} for thresHeight {thresHeight}") 

findOnePeak(dataframe, 0, 190, 0)