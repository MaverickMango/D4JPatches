/*
 * Copyright (c) 2007 Mockito contributors
 * This program is made available under the terms of the MIT License.
 */
package org.mockito.internal.verification.argumentmatching;

import java.util.LinkedList;
import java.util.List;

import org.hamcrest.Matcher;
import org.hamcrest.StringDescription;
import org.mockito.internal.matchers.ContainsExtraTypeInformation;

@SuppressWarnings("unchecked")
public class ArgumentMatchingTool {

    /**
     * Suspiciously not matching arguments are those that don't much, the toString() representation is the same but types are different.
     */
    public Integer[] getSuspiciouslyNotMatchingArgsIndexes(List<Matcher> matchers, Object[] arguments) {
        if (matchers.size() != arguments.length) {
            return new Integer[0];
        }
        
        List<Integer> suspicious = new LinkedList<Integer>();
        int i = 0;
        for (Matcher m : matchers) {
            if (m instanceof ContainsExtraTypeInformation 
                    && !safelyMatches(m, arguments[i]) 
                    && toStringEquals(m, arguments[i])
                    && !((ContainsExtraTypeInformation) m).typeMatches(arguments[i])) {
                suspicious.add(i);
            }
            i++;
        }
        return suspicious.toArray(new Integer[0]);
    }

    private boolean safelyMatches(Matcher m, Object arg) {
        try {
            return m.matches(arg);
        } catch (Throwable t) {
            return false;
        }
    }

 protected void toStringEquals ( Matcher m , java.lang.String [ ] VAR_2 , boolean VAR_3 ) { init ( ) ; boolean VAR_4 = false ; Object VAR_5 = null ; for ( int i = 0 ; i < VAR_2 . length ; i ++ ) { if ( STRING_1 . equals ( VAR_2 [ i ] ) ) { VAR_4 = true ; VAR_6 . add ( STRING_1 ) ; } else if ( STRING_2 . equals ( VAR_2 [ i ] ) ) { VAR_6 . add ( STRING_2 ) ; } } else if ( 
}
