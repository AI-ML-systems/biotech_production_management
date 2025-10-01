# Project general coding guidelines

## Code Quality

- Use meaningful variable and function names that clearly describe their purpose
- Include helpful comments for complex logic

## Writing Code

- The primary design principles to follow are the SOLID principles. A seminal reference is Robert C. Martin’s “Clean Code.”
- Use the Abstract Factory pattern when:
  - a system should be independent of how its product are created, composed and represented.
  - a system should be configured with one of multiple families of products.
  - a family of related product objects is designed to be used together, and you need to enforce this constraint.
  - you want to provide a class library of products, and you want to reveal just their interfaces, not their implementations.

- Use Builder pattern when:
  - the algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled.
  - the construction process must allow different representations for the object that's constructed.

- Use Factory Method pattern when:
  - a class can't anticipate the class of objects it must create.
  - a class wants its subclasses to specify the objects it creates.
  - classes delegate responsibility to one of several helper subclasses, and you want to localize the knowledge of which helper subclass is the delegate.

- Use the Prototype pattern when a system should be independent of how its products are created, composed, and represented; and
  - when the classes to instantiate are specified at run-time, for example, by dynamic loading; or
  - to avoid building a class hierarchy of factories that parallels the class hierarchy or products; or
  - when instances of a class can have one of only a few different combinations of state. It may be more convenient to install a corresponding number of prototypes and clone them rather than instantiating the class manually, each time with the appropriate state.

## Architecture

- When designing modules/functions/classes/interfaces, start with maximum privacy. Expose methods or make variables public only when necessary. Assume everything is private by default. Motivation: this preserves encapsulation. A private method can always be made public later without breaking clients. Doing the opposite may fail or require heavy refactoring because public APIs might already be in use (over long time spans).
- Don’t overuse OOP; often a free function is enough. Start by designing simple functions, then group them into meaningful modules. If you notice coherent entities within a module’s functions, you can turn them into a class with methods. Use exploratory/spike coding: write quick, rough code first to discover problems, then start fresh once you know which methods/classes/algorithms you need. Motivation: the simpler the unit, the easier it is to maintain contracts and test. Classes are harder to test than modules, and modules harder than functions.
- Adhere to contracts (preconditions, postconditions, invariants) and encapsulation. In classes, every method must leave the object in a valid state—that’s the invariant. We encapsulate data to ensure integrity inside the class; the outside world can’t guarantee it. Reading: “Design Patterns” by the Gang of Four; https://refactoring.guru/design-patterns. A seminal book that teaches elegant solutions to common problems.
