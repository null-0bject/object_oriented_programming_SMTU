from Server import Server
from Data import Data
from Router import Router


if __name__ == '__main__':
    assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(Router,
                'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
    assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(Server,
            'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"
    router = Router()
    sv_from = Server()
    sv_from2 = Server()
    router.link(sv_from)
    router.link(sv_from2)
    router.link(Server())
    router.link(Server())
    sv_to = Server()
    router.link(sv_to)
    sv_from.send_data(Data("Hello", sv_to.get_ip()))
    sv_from2.send_data(Data("Hello", sv_to.get_ip()))
    sv_to.send_data(Data("Hi", sv_from.get_ip()))
    router.send_data()
    msg_lst_from = sv_from.get_data()
    msg_lst_to = sv_to.get_data()
    assert len(router.get_data()) == 0, "после отправки сообщений буфер в роутере должен очищаться"
    assert len(sv_from.get_buffer()) == 0, "после получения сообщений буфер сервера должен очищаться"
    assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"
    assert msg_lst_from[0] == "Hi" and msg_lst_to[
        0] == "Hello", "данные не прошли по сети, классы не функционируют должным образом"
    assert hasattr(router, '_Router__buffer') and hasattr(sv_to,
            '_Server__buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"
    router.unlink(sv_to)
    sv_from.send_data(Data("Hello", sv_to.get_ip()))
    router.send_data()
    msg_lst_to = sv_to.get_buffer()
    assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"