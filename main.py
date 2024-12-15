from dfa import DFA


def get_custom_dfa():
    print("Kendi DFA'nızı tanımlayın.")

    states = input("Durumları virgül ile ayrılmış şekilde giriniz (örn: q0,q1,q2): ").strip().split(',')

    alphabet = input("Alfabeyi virgül ile ayrılmış şekilde giriniz (örn: 0,1): ").strip().split(',')

    transitions = {}
    print("Geçiş fonksiyonlarını giriniz. Format: <kaynak_durum>,<sembol>,<hedef_durum>")
    print("Örn: q0,0,q1 (durumları bitirmek için 'done' yazınız)")
    while True:
        transition_input = input("Geçiş: ").strip()
        if transition_input.lower() == "done":
            break
        try:
            source, symbol, target = transition_input.split(',')
            transitions[(source, symbol)] = target
        except ValueError:
            print("Hatalı format! Lütfen <kaynak_durum>,<sembol>,<hedef_durum> formatında giriniz.")

    start_state = input("Başlangıç durumunu giriniz: ").strip()

    accept_states = input("Kabul durumlarını virgül ile ayrılmış şekilde giriniz (örn: q2,q3): ").strip().split(',')

    return DFA(states, alphabet, transitions, start_state, accept_states)


def get_predefined_dfa():
    print("Hazır bir DFA kullanılıyor.")
    states = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5']
    alphabet = ['0', '1']
    transitions = {
        ('q0', '0'): 'q1',
        ('q0', '1'): 'q2',
        ('q1', '0'): 'q2',
        ('q1', '1'): 'q3',
        ('q2', '0'): 'q3',
        ('q2', '1'): 'q4',
        ('q3', '0'): 'q3',
        ('q3', '1'): 'q3',
        ('q4', '0'): 'q4',
        ('q4', '1'): 'q4',
        ('q5', '0'): 'q5',
        ('q5', '1'): 'q4',
    }
    start_state = 'q0'
    accept_states = ['q3', 'q4']
    return DFA(states, alphabet, transitions, start_state, accept_states)


def main():
    print("DFA Minimizasyon Programı")
    print("1. Hazır bir DFA kullan")
    print("2. Kendi DFA'nı tanımla")
    choice = input("Seçiminizi yapınız (1 veya 2): ").strip()

    if choice == "1":
        dfa = get_predefined_dfa()
    elif choice == "2":
        dfa = get_custom_dfa()
    else:
        print("Geçersiz seçim! Program sonlandırılıyor.")
        return

    print("\nOrijinal DFA:")
    print("Durumlar:", dfa.states)
    print("Geçişler:", dfa.transitions)
    print("Kabul Durumları:", dfa.accept_states)

    dfa.minimize()

    print("\nMinimize Edilmiş DFA:")
    print("Durumlar:", dfa.states)
    print("Geçişler:", dfa.transitions)
    print("Kabul Durumları:", dfa.accept_states)


if __name__ == "__main__":
    main()
