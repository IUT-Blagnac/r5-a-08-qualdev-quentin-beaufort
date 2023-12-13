package dojo;

import java.util.ArrayList;
import java.util.List;

public class Order {
    protected String owner;
    protected String target;
    protected List<String> cocktails = new ArrayList<String>();

    public Order() {
    }

    public List<String> getCocktails() {
        return cocktails;
    }

    public String getOwner() {
        return owner;
    }

    public void declareOwner(String owner) {
        this.owner = owner;
    }

    public String getTarget() {
        return target;
    }

    public void declareTarget(String target) {
        this.target = target;
    }
}
