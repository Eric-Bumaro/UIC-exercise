
public class GUI{
    public static void main(String[] args) {
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run(){
                        try {
                        	Bank bank = new Bank("UIC Bank");
                            ControllerGetMoney controller=new ControllerGetMoney(bank);//the previous
                            ViewGetMoney viewSimple=new ViewGetMoney(bank,controller);
                            ControllerWithdraw controller1=new ControllerWithdraw(bank);
                            ViewWithdraw viewWithdraw=new ViewWithdraw(bank,controller1);
                            ControllerCreate controller2=new ControllerCreate(bank);
                            ViewCreate viewCreate=new ViewCreate(bank,controller2);
                            ControllerHistory controller3=new ControllerHistory(bank);
                            ViewHistory viewHistroy=new ViewHistory(bank,controller3);
        				} catch (Exception e) {
        					// TODO Auto-generated catch block
        					e.printStackTrace();
        				}
            }
        });
    }
}