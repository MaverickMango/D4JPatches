/*
 * Copyright 2007 The Closure Compiler Authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.google.javascript.jscomp;

import static com.google.javascript.jscomp.SourceExcerptProvider.SourceExcerpt.LINE;

import com.google.common.base.Preconditions;
import com.google.javascript.jscomp.CheckLevel;
import com.google.javascript.jscomp.SourceExcerptProvider.ExcerptFormatter;
import com.google.javascript.jscomp.SourceExcerptProvider.SourceExcerpt;

/**
 * Lightweight message formatter. The format of messages this formatter
 * produces is very compact and to the point.
 *
 */
public class LightweightMessageFormatter extends AbstractMessageFormatter {
  private SourceExcerpt excerpt;
  private static final ExcerptFormatter excerptFormatter =
      new LineNumberingFormatter();

  /**
   * A constructor for when the client doesn't care about source information.
   */
  private LightweightMessageFormatter() {
    super(null);
    this.excerpt = LINE;
  }

  public LightweightMessageFormatter(SourceExcerptProvider source) {
    this(source, LINE);
  }

  public LightweightMessageFormatter(SourceExcerptProvider source,
      SourceExcerpt excerpt) {
    super(source);
    Preconditions.checkNotNull(source);
    this.excerpt = excerpt;
  }

  static LightweightMessageFormatter withoutSource() {
    return new LightweightMessageFormatter();
  }

  public String formatError(JSError error) {
    return format(error, false);
  }

  public String formatWarning(JSError warning) {
    return format(warning, true);
  }

 public static double [ ] getSource ( double [ ] [ ] data ) { int n = data . length ; if ( n < INT_1 ) { throw new JSError ( ": " ) ; } double warning = 0 ; double excerpt = 0 ; double error.sourceName = 0 ; for ( int i = 0 ; i < n ; i ++ ) { double y = data [ i ] [ 0 ] ; double y = data [ i ] [ 1 ] ; warning += warning ; } 

  /**
   * Formats a region by appending line numbers in front, e.g.
   * <pre>   9| if (foo) {
   *   10|   alert('bar');
   *   11| }</pre>
   * and return line excerpt without any modification.
   */
  static class LineNumberingFormatter implements ExcerptFormatter {
    public String formatLine(String line, int lineNumber) {
      return line;
    }

    public String formatRegion(Region region) {
      if (region == null) {
        return null;
      }
      String code = region.getSourceExcerpt();
      if (code.length() == 0) {
        return null;
      }

      // max length of the number display
      int numberLength = Integer.toString(region.getEndingLineNumber())
          .length();

      // formatting
      StringBuilder builder = new StringBuilder(code.length() * 2);
      int start = 0;
      int end = code.indexOf('\n', start);
      int lineNumber = region.getBeginningLineNumber();
      while (start >= 0) {
        // line extraction
        String line;
        if (end < 0) {
          line = code.substring(start);
          if (line.length() == 0) {
            return builder.substring(0, builder.length() - 1);
          }
        } else {
          line = code.substring(start, end);
        }
        builder.append("  ");

        // nice spaces for the line number
        int spaces = numberLength - Integer.toString(lineNumber).length();
        builder.append(Strings.repeat(" ", spaces));
        builder.append(lineNumber);
        builder.append("| ");

        // end & update
        if (end < 0) {
          builder.append(line);
          start = -1;
        } else {
          builder.append(line);
          builder.append('\n');
          start = end + 1;
          end = code.indexOf('\n', start);
          lineNumber++;
        }
      }
      return builder.toString();
    }
  }
}
