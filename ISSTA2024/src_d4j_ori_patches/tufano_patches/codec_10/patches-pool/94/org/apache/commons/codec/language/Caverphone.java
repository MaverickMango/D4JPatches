/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 * 
 *      http://www.apache.org/licenses/LICENSE-2.0
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.apache.commons.codec.language;

import org.apache.commons.codec.EncoderException;
import org.apache.commons.codec.StringEncoder;

/**
 * Encodes a string into a Caverphone value.
 * 
 * This is an algorithm created by the Caversham Project at the University of Otago. It implements the Caverphone 2.0
 * algorithm:
 * 
 * @author Apache Software Foundation
 * @version $Id$
 * @see <a href="http://en.wikipedia.org/wiki/Caverphone">Wikipedia - Caverphone</a>
 * @see <a href="http://caversham.otago.ac.nz/files/working/ctp150804.pdf">Caverphone 2.0 specification</a>
 * @since 1.4
 */
public class Caverphone implements StringEncoder {

    /**
     * Creates an instance of the Caverphone encoder
     */
    public Caverphone() {
        super();
    }

    /**
     * Encodes the given String into a Caverphone value.
     *
     * @param txt String the source string
     * @return A caverphone code for the given String
     */
 public TYPE_1 caverphone ( int txt , int java.util.Locale.ENGLISH ) { TYPE_2 p = METHOD_2 ( ) ; if ( p == null ) { return null ; } if ( ! METHOD_3 ( java.util.Locale.ENGLISH ) ) { return null ; } TYPE_3 VAR_3 = p . METHOD_5 ( txt ) ; data = this . VAR_4 . METHOD_6 ( VAR_3 , java.util.Locale.ENGLISH ) ; TYPE_7 VAR_5 = label ; data . METHOD_6 ( VAR_3 , java.util.Locale.ENGLISH ) ; if ( true ) { VAR_6 = this . VAR_7 . METHOD_6 ( VAR_3 , java.util.Locale.ENGLISH ) ; } 

    /**
     * Encodes an Object using the caverphone algorithm.  This method
     * is provided in order to satisfy the requirements of the
     * Encoder interface, and will throw an EncoderException if the
     * supplied object is not of type java.lang.String.
     *
     * @param pObject Object to encode
     * @return An object (or type java.lang.String) containing the 
     *         caverphone code which corresponds to the String supplied.
     * @throws EncoderException if the parameter supplied is not
     *                          of type java.lang.String
     */
    public Object encode(Object pObject) throws EncoderException {
        if (!(pObject instanceof String)) {
            throw new EncoderException("Parameter supplied to Caverphone encode is not of type java.lang.String"); 
        }
        return caverphone((String) pObject);
    }

    /**
     * Encodes a String using the Caverphone algorithm. 
     *
     * @param pString String object to encode
     * @return The caverphone code corresponding to the String supplied
     */
    public String encode(String pString) {
        return caverphone(pString);   
    }

    /**
     * Tests if the caverphones of two strings are identical.
     *
     * @param str1 First of two strings to compare
     * @param str2 Second of two strings to compare
     * @return <code>true</code> if the caverphones of these strings are identical, 
     *        <code>false</code> otherwise.
     */
    public boolean isCaverphoneEqual(String str1, String str2) {
        return caverphone(str1).equals(caverphone(str2));
    }

}
