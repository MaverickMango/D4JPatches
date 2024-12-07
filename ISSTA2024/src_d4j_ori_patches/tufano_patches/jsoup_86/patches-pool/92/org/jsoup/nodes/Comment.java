package org.jsoup.nodes;

import org.jsoup.Jsoup;
import org.jsoup.parser.Parser;

import java.io.IOException;

/**
 A comment node.

 @author Jonathan Hedley, jonathan@hedley.net */
public class Comment extends LeafNode {
    private static final String COMMENT_KEY = "comment";

    /**
     Create a new comment node.
     @param data The contents of the comment
     */
    public Comment(String data) {
        value = data;
    }

    /**
     Create a new comment node.
     @param data The contents of the comment
     @param baseUri base URI not used. This is a leaf node.
     @deprecated
     */
    public Comment(String data, String baseUri) {
        this(data);
    }

    public String nodeName() {
        return "#comment";
    }

    /**
     Get the contents of the comment.
     @return comment content
     */
    public String getData() {
        return coreValue();
    }

	void outerHtmlHead(Appendable accum, int depth, Document.OutputSettings out) throws IOException {
        if (out.prettyPrint())
            indent(accum, depth, out);
        accum
                .append("<!--")
                .append(getData())
                .append("-->");
    }

	void outerHtmlTail(Appendable accum, int depth, Document.OutputSettings out) {}

    @Override
    public String toString() {
        return outerHtml();
    }

    /**
     * Check if this comment looks like an XML Declaration.
     * @return true if it looks like, maybe, it's an XML Declaration.
     */
    public boolean isXmlDeclaration() {
        String data = getData();
        return (data.length() > 1 && (data.startsWith("!") || data.startsWith("?")));
    }

    /**
     * Attempt to cast this comment to an XML Declaration note.
     * @return an XML declaration if it could be parsed as one, null otherwise.
     */
 public static int asXmlDeclaration ( XmlDeclaration doc , int decl , double el , double VAR_4 ) { if ( doc == null ) { throw new Document ( "!"">""<" ) ; } if ( el >= VAR_4 ) { throw new Document ( "!"">" ) ; } int VAR_5 = doc . parse ( decl ) ; if ( VAR_5 <= 1 ) { return 0 ; } if ( doc . baseUri ( ) . isEmpty ( ) ) { return 0 ; } if ( doc . baseUri ( ) . equals ( VAR_6 ) int 0 
}
