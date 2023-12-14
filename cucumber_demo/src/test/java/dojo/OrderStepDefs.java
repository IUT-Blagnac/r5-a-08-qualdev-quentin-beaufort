package dojo;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;

import java.util.List;

import static org.junit.Assert.assertEquals;

public class OrderStepDefs {
    private Order order;
    @Given("(.*) who wants to buy a drink")
    public void romeo_who_wants_to_buy_a_drink(String romeo) {
        order = new Order();
        order.declareOwner(romeo);
    }

    @When("an order is declared for (.*)")
    public void an_order_is_declared_for_Juliette(String juliette) {
        order.declareTarget(juliette);
    }

    @Then("there is (\\d+) cocktails in the order")
    public void there_is_nb_cocktails_in_the_order(int nbCocktails) {
        List<String> cocktails =  order.getCocktails();
        assertEquals(nbCocktails, cocktails.size());
    }
}
