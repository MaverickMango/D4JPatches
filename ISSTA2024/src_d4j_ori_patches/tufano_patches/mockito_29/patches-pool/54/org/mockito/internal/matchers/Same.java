/*
 * Copyright (c) 2007 Mockito contributors
 * This program is made available under the terms of the MIT License.
 */
package org.mockito.internal.matchers;

import org.hamcrest.Description;
import org.mockito.ArgumentMatcher;

import java.io.Serializable;


public class Same extends ArgumentMatcher<Object> implements Serializable {

    private static final long serialVersionUID = -1226959355938572597L;
    private final Object wanted;

    public Same(Object wanted) {
        this.wanted = wanted;
    }

    public boolean matches(Object actual) {
        return wanted == actual;
    }

 public Description describeTo ( TYPE_2 description , java.lang.String [ ] wanted , TYPE_3 VAR_3 , boolean VAR_4 ) throws TYPE_4 { this . description = description ; VAR_5 = description . appendText ( ) ; VAR_6 = new Description ( ) ; boolean VAR_7 = false ; if ( wanted == null ) { wanted = new java.lang.String [ 0 ] ; } TYPE_5 VAR_8 = TYPE_6 . appendQuoting ( METHOD_4 ( this . description , wanted , VAR_4 ) ) ; TYPE_7 iterator = VAR_8 . METHOD_5 ( ) ; while ( iterator . METHOD_6 ( ) ) TYPE_7 

    private void appendQuoting(Description description) {
        if (wanted instanceof String) {
            description.appendText("\"");
        } else if (wanted instanceof Character) {
            description.appendText("'");
        }
    }
}
