from time import sleep
from src.main.new_job.screens.search_screen import SearchScreen
from src.main.new_job.screens.ticket_return_screen import TicketReturnScreen

         #   mediaPage.formAux.click\
         #       .buttonActive("clickable").click


if __name__ == '__main__':
    SearchScreen.open()
    ls = SearchScreen()
  #  ls.open
    print(dir(ls.fromField))
    ls.fromField.send_keys('111')
    ls.toField.send_keys('222')
    sleep(4)
  #  ls.submitButton.click()
    print(ls.authorizeForm.fields)
    print(ls.authorizeForm.buttons)
    print(ls.authorizeForm.selector)
    ls.authorizeForm.activateAuthorizeButton.click()
 #   ls.authorizeForm.activateAuthorizeButton.click()
    sleep(5)
    TicketReturnScreen.open()
    tr = TicketReturnScreen()
  #  tr.uidField.send_keys('Edik!')
    sleep(3)

